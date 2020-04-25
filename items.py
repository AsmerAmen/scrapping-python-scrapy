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


class AmazonItemSubcategory(scrapy.Item):
    # Amazon Product
    link = scrapy.Field()
    image_link = scrapy.Field()
    amazon_certified = scrapy.Field()
    category = scrapy.Field()


class AmazonItemProduct(scrapy.Item):
    link = scrapy.Field()
    name = scrapy.Field()
    provider = scrapy.Field()
    price = scrapy.Field()
    category = scrapy.Field()





