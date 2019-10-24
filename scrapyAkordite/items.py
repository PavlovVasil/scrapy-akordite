# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyakorditeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    songName = scrapy.Field()
    artist = scrapy.Field()
    chords = scrapy.Field()
