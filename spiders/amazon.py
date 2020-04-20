# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazonItem


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    # allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com/s?bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&fst=as%3Aoff&qid=1587316220&rnid=1250225011&ref=lp_283155_nr_p_n_publication_date_0']

    def parse(self, response):
        items = AmazonItem()

        name = response.css('.a-color-base.a-text-normal::text').extract()
        # author = response.css('.a-row .a-size-base .a-color-secondary').css('.a-size-base .a-link-normal').css('::text').extract()
        author = response.css('.sg-col-12-of-28 .a-color-secondary .a-size-base:nth-child(2)').css('::text').extract()
        # price = response.css('').extract()
        image_link = response.css('.s-image::attr(src)').extract()


        print(len(name))
        print(len(author))
        for index, row in enumerate(author):
            author[index] = row.strip()
        print(name)
        print(author)
        print(image_link)

        # items['name'] = name
        # items['author'] = author
        # items['price'] = price
        # items['image_link'] = image_link
