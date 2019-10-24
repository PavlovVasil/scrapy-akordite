# -*- coding: utf-8 -*-
import scrapy
from scrapyAkordite.items import ScrapyakorditeItem
from bs4 import BeautifulSoup as soup, Tag, NavigableString


class AkorditeCrawlerSpider(scrapy.Spider):
    name = 'akordite_crawler'
    allowed_domains = ['akordite.com']
    start_urls = ['http://www.akordite.com/index.php?option=com_chordbase&Itemid=26&initial=&limit=1548&limitstart=0']

    def parse(self, response):
        songs = response.css("#mainbody table.mainbody td.mainbody .padding table:nth-of-type(2) tr")
        for song in songs[1:]:
            songItem = ScrapyakorditeItem()
            songItem['songName'] = song.css('a::text').get()
            songItem['artist'] = song.css('td:nth-child(2)::text').get()
            linkUrl = song.css("a::attr(href)").get()
            fullUrl = 'http://www.akordite.com/' + linkUrl
            yield scrapy.Request(fullUrl, callback=self.parse_content, meta = {'songItem': songItem})
        
        #yield scrapy.Request("http://www.akordite.com/index.php?option=com_chordbase&Itemid=26&task=viewSong&song_id=194065", 
        #callback=self.parse_content, meta = {'songItem': songItem})


    def parse_content(self, response):
        songItem = response.meta.get('songItem')
        songItem['chords'] = response.css('#mainbody table.mainbody tr td.mainbody div.Song').get()
        yield songItem