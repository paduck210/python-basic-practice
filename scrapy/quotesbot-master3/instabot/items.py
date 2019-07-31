# -*- coding: utf-8 -*-

# Define here the models for your scraped items
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class InstaTagCount(scrapy.Item):
    # define the fields for your item here like:
    tag_name = scrapy.Field()
    tag_count = scrapy.Field()
    tag_date = scrapy.Field()
    pass
