# -*- coding: utf-8 -*-
import scrapy
from scrapyAkordite.items import ScrapyakorditeItem


class AkorditeCrawlerSpider(scrapy.Spider):
    name = 'akordite_crawler'
    allowed_domains = ['akordite.com']
    start_urls = ['http://www.akordite.com/index.php?option=com_chordbase&Itemid=26&initial=&limit=15&limitstart=0']

    def parse(self, response):
        songs = response.css("#mainbody table.mainbody td.mainbody .padding table:nth-of-type(2) tr")
        for song in songs[1:]:
            songItem = ScrapyakorditeItem()
            songItem['songName'] = song.css('a::text').get()
            songItem['artist'] = song.css('td:nth-child(2)::text').get()
            linkUrl = song.css("a::attr(href)").get()
            #if linkUrl is not None:
            fullUrl = 'http://www.akordite.com/' + linkUrl
            pass