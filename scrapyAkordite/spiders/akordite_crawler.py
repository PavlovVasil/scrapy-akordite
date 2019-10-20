# -*- coding: utf-8 -*-
import scrapy


class AkorditeCrawlerSpider(scrapy.Spider):
    name = 'akordite_crawler'
    allowed_domains = ['akordite.com']
    start_urls = ['http://akordite.com/']

    def parse(self, response):
        pass
