# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ApkSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    AppName = scrapy.Field()
    name = scrapy.Field()  # app name
    size = scrapy.Field() # app size
    file_urls = scrapy.Field()
    version=scrapy.Field()
    tags=scrapy.Field()
    file_paths=scrapy.Field()
    #files = scrapy.Field()
