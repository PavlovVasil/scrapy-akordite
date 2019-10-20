# -*- coding: utf-8 -*-
import scrapy


class AkorditeCrawlerSpider(scrapy.Spider):
    name = 'akordite_crawler'
    allowed_domains = ['akordite.com']
    start_urls = ['http://www.akordite.com/index.php?option=com_chordbase&Itemid=26&initial=&limit=1527&limitstart=0']

    def parse(self, response):
        pass
