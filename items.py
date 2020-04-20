# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SpyderUnoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # Spyder tutorial
    title = scrapy.Field()
    author = scrapy.Field()
    tag = scrapy.Field()


class AmazonItem(scrapy.Item):
    # Amazon
    name = scrapy.Field()
    author = scrapy.Field()
    price = scrapy.Field()
    image_link = scrapy.Field()


