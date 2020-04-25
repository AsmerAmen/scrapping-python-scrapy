import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser

from ..items import SpyderUnoItem


class QuoteSpyder(scrapy.Spider):
    name = 'spyder'
    start_urls = [
        # 'http://quotes.toscrape.com'
        'http://quotes.toscrape.com/login'
    ]

    def parse(self, response):
        token = response.css('form input::attr(value)').extract_first()
        # print(token)
        return FormRequest.from_response(response,
                                         formdata={
                                            'csrf_token': token,
                                            'username': 'asmer.amenar@gmail.com',
                                            'password': 'password'
                                         },
                                         callback=self.start_scraping)

    def start_scraping(self, response):
        # open_in_browser(response)
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

        # next_page = response.css('li.next a::attr(href)').get()
        #
        # if next_page:
        #     yield response.follow(next_page, self.parse)
