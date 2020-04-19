import scrapy
from ..items import SpyderUnoItem


class QuoteSpyder(scrapy.Spider):
    name = 'spyder'
    start_urls = [
        'http://quotes.toscrape.com/'
        ]

    def parse(self, response):
        items = SpyderUnoItem()

        all_div_quotes = response.css('div.quote')

        for quote in all_div_quotes:
            title = quote.css('span.text::text').extract()
            author = quote.css('.author::text').extract()
            tag = quote.css('.tag::text').extract()

            items['title'] = title
            items['author'] = author
            items['tag'] = tag

            yield items

        next_page = response.css('li.next a::attr(href)').get()

        if next_page:
            yield response.follow(next_page, self.parse)
