# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import Rule
from scrapy.utils.response import open_in_browser
from scrapy.linkextractors import LinkExtractor
from ..items import AmazonItemProduct, AmazonItemSubcategory
import sqlite3


class AmazonSpiderSubcategory(scrapy.Spider):
    name = 'amazon_subcategory'
    start_urls = ['https://www.amazon.com/s?i=specialty-aps&srs=13575748011&qid=1587677057&ref=sr_pg_2']
    page_number = 2
    total_number_of_pages = 0

    def parse(self, response):
        items = AmazonItemSubcategory()

        products = response.css('div.s-latency-cf-section')

        print('Number of section:', len(products))

        category = response.css('#searchDropdownBox > option::text').extract_first()

        # total_number_of_pages = 0
        later_pages = response.css('li+ .a-disabled::text').extract()
        # total_number_of_pages = int(later_pages[0])if len(later_pages) > 0 and isinstance(later_pages[0], int) else 0
        # first_page = response.css('.pagnDisabled::text').extract()
        AmazonSpiderSubcategory.total_number_of_pages = int(later_pages[0]) if len(later_pages) > 0 \
            else AmazonSpiderSubcategory.total_number_of_pages

        for product in products:
            link = product.css('a.a-text-normal::attr(href)').extract()
            image_link = product.css('.s-image-fixed-height .s-image::attr(src)').extract()
            amazon_certified = product.css('.a-color-state').css('::text').extract()

            items['link'] = link
            items['image_link'] = image_link
            items['amazon_certified'] = amazon_certified
            items['category'] = category

            yield items

            next_page = 'https://www.amazon.com/s?i=specialty-aps&srs=13575748011&page={}&qid=1587677102&ref=sr_pg_2'\
                .format(AmazonSpiderSubcategory.page_number)
            if AmazonSpiderSubcategory.page_number <= AmazonSpiderSubcategory.total_number_of_pages:
                AmazonSpiderSubcategory.page_number += 1
                yield response.follow(next_page, self.parse)


class AmazonSpiderProduct(scrapy.Spider):
    name = 'amazon_product'
    # allowed_domains = ['amazon.com']
    conn = sqlite3.connect("amazon.db")
    cur = conn.cursor()

    links = cur.execute("""SELECT link from smart_home_db""").fetchall()

    start_urls = [link[0] for link in links]

    def parse(self, response):
        items = AmazonItemProduct()

        link = response.request.url
        name = response.css('span#productTitle::text').extract()
        provider = response.css('#bylineInfo::text').extract()
        price = response.css(
            '#sh-badge-v2-simple-total-price, #olp-upd-new .a-color-price, #comparison_price_row .a-text-bold'
        ).css('::text').extract()

        for index, row in enumerate(name):
            name[index] = row.strip()

        for index, row in enumerate(price):
            price[index] = float(row.strip().replace('From', '').replace('$', ''))

        print(name)
        print(provider)
        print(price)

        items['link'] = link
        items['name'] = name
        items['provider'] = provider
        items['price'] = price

        yield items


class AmazonSpiderCrawler(scrapy.spiders.CrawlSpider):
    name = 'amazon_crawler'
    start_urls = ['https://www.amazon.com/gp/browse.html?node=6563140011&ref_=nav_em_0_2_8_2_amazon_smart_home']

    products_links = []

    rules = (
        # Extract links matching 'category.php' (but not matching 'subsection.php')
        # and follow links from them (since no callback means follow=True by default).
        # Rule(LinkExtractor(restrict_css=('.bxc-grid__column--1-of-5.bxc-grid__column--light, #pagnNextString',)
        #                    ),
        #      ),

        # Extract links matching 'item.php' and parse them with the spider's method parse_item
        Rule(LinkExtractor(
            # allow=('item\.php',)
            restrict_css=('.bxc-grid__column--1-of-5.bxc-grid__column--light',),
            ),
             callback='parse_category'
        ),
        # Rule(LinkExtractor(
        #     # allow=('item\.php',)
        #     restrict_css=('a.a-text-normal',),
        # ),
        #     callback='parse_product'
        # ),
    )

    def parse_product(self, response):
        name = response.css('span#productTitle::text').extract()
        provider = response.css('#bylineInfo::text').extract()
        price = response.css(
            '#sh-badge-v2-simple-total-price, #olp-upd-new .a-color-price, #comparison_price_row .a-text-bold'
        ).css('::text').extract()

        for index, row in enumerate(name):
            name[index] = row.strip()

        for index, row in enumerate(price):
            price[index] = float(row.strip().replace('From', '').replace('$', '').replace(',', ''))

        print(name)
        print(provider)
        print(price)


    def parse_category(self, response):
        # open_in_browser(response)
        self.logger.info('Hi, this is an item page! %s', response.url)

        # print('Asmer: %s' % response.css('a.a-text-normal::attr(href)').extract())
        products_links = response.css('a.a-text-normal::attr(href)').extract()

        if len(products_links) > 0:
            for link in products_links:
                AmazonSpiderCrawler.products_links.append(link)
        print(len(AmazonSpiderCrawler.products_links))

        next_page = response.css('.pagnNext, .a-last a').css('::attr(href)').extract_first()
        print(next_page)
        if next_page:
            yield response.follow(next_page, self.parse_category)


        # print(response.meta['link_text'])
        # item = scrapy.Item()
        # item['id'] = response.xpath('//td[@id="item_id"]/text()').re(r'ID: (\d+)')
        # item['name'] = response.xpath('//td[@id="item_name"]/text()').get()
        # item['description'] = response.xpath('//td[@id="item_description"]/text()').get()
        # item['link_text'] = response.meta['link_text']
        # return item




