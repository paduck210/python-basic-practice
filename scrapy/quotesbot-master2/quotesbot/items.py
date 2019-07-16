# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QuotesbotItem(scrapy.Item):
    # define the fields for your item here like:
    author = scrapy.Field()
    tags = scrapy.Field()
    text = scrapy.Field()
    author_name = scrapy.Field()
    author_born = scrapy.Field()
    author_description = scrapy.Field()
    pass


