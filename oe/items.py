# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class OeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
    school = scrapy.Field()
    st_core = scrapy.Field()
    st_related = scrapy.Field()
    country = scrapy.Field()
    url = scrapy.Field()
    year = scrapy.Field()



