# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazonItem


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    # allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com/lighting-fans-works-with-alexa/b/ref=s9_acss_bw_cg_SHnav_2a1_w?ie=UTF8&node=13575748011&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-4&pf_rd_r=D8XG9GRM62XC3EFTESHT&pf_rd_t=101&pf_rd_p=692dc65d-102a-4ec7-ae02-609cf91cfed8&pf_rd_i=6563140011']
    page_number = 1
    total_number_of_pages = 0

    def parse(self, response):
        items = AmazonItem()
        if AmazonSpider.page_number > 1:
            products = response.css('.s-result-item')
        else:
            products = response.css('.s-result-item.celwidget')

        print('Number of section:', len(products))

        category = response.css('#searchDropdownBox > option::text').extract_first()

        # total_number_of_pages = 0
        # later_pages = response.css('.a-disabled::text').extract()
        # total_number_of_pages = int(later_pages[0])if len(later_pages) > 0 and isinstance(later_pages[0], int) else 0
        first_page = response.css('.pagnDisabled::text').extract()
        AmazonSpider.total_number_of_pages = int(first_page[0]) if len(first_page) > 0 \
            else AmazonSpider.total_number_of_pages

        for product in products:
            if AmazonSpider.page_number > 1:
                name = product.css('span.a-text-normal::text').extract()
                provider = product.css('.a-color-secondary+ .a-color-secondary').css('::text').extract()
                price = product.css('.a-size-base::text').extract()
                image_link = product.css('.s-image-fixed-height .s-image::attr(src)').extract()
                amazon_certified = product.css('.a-text-bold').css('::text').extract()
            else:
                name = product.css('.s-access-title::text').extract()
                provider = product.css('.a-color-secondary+ .a-color-secondary').css('::text').extract()
                price = product.css('.a-size-base::text').extract()
                image_link = product.css('.cfMarker::attr(src)').extract()
                amazon_certified = product.css('.a-text-bold').css('::text').extract()

            items['name'] = name
            items['provider'] = provider
            items['price'] = price
            items['image_link'] = image_link
            items['amazon_certified'] = amazon_certified
            items['category'] = category

            yield items
            AmazonSpider.page_number += 1
            next_page = 'https://www.amazon.com/s?i=specialty-aps&srs=13575748011&page={}&qid=1587663347&swrs=67F5AD12950A1B3764A53CDF752C3D8B&ref=sr_pg_3'.format(AmazonSpider.page_number)
            if AmazonSpider.page_number <= AmazonSpider.total_number_of_pages:
                yield response.follow(next_page, self.parse)



            # print(len(name))
            # print(len(provider))
            # print(len(price))
            # for index, row in enumerate(provider):
            #     provider[index] = row.strip()
            # print(name)
            # print(provider)
            # print(image_link)
            # print(price)

        # items['name'] = name
        # items['provider'] = provider
        # items['price'] = price
        # items['image_link'] = image_link
