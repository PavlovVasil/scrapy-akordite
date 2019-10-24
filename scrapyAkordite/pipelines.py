# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3

class ScrapyakorditePipeline(object):
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect('akordite.db')
        self.c = self.conn.cursor()

    def create_table(self):
        self.c.execute('DROP TABLE IF EXISTS songs')
        self.c.execute('''CREATE TABLE songs(
            songName text, 
            artist text,
            chords text
            )''')

    def store_db(self, item):
        self.c.execute('''INSERT INTO songs VALUES(?,?,?)''',(
            item['songName'],
            item['artist'],
            item['chords']
        ))
        self.conn.commit()

    def process_item(self, item, spider):
        self.store_db(item)
        return item