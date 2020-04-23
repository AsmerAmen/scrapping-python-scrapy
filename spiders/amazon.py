# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazonItem


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    # allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com/lighting-fans-works-with-alexa/b/ref=s9_acss_bw_cg_SHnav_2a1_w?ie=UTF8&node=13575748011&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-4&pf_rd_r=D8XG9GRM62XC3EFTESHT&pf_rd_t=101&pf_rd_p=692dc65d-102a-4ec7-ae02-609cf91cfed8&pf_rd_i=6563140011']
    
    def parse(self, response):
        items = AmazonItem()

        products = response.css('.s-result-item.celwidget')
        print('Number of section:', len(products))

        for product in products:
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

            yield items


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
