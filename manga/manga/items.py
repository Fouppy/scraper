# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class MangaItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    description = scrapy.Field()
    release_date = scrapy.Field()
    author = scrapy.Field()
    editor = scrapy.Field()
    isbn = scrapy.Field()
    collection = scrapy.Field()
    pages = scrapy.Field()
    cover = scrapy.Field()
