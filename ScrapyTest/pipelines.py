# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3
from os import path

from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher

class ScrapytestPipeline(object):
    def process_item(self, item, spider):
        return item


class SQLitePipeline(object):
    file_name = 'data.sqlite'

    def __init__(self):
        self.conn = None
        dispatcher.connect(self.initialize, signals.engine_started)
        dispatcher.connect(self.finalize, signals.engine_stopped)

    def initialize(self):
        if path.exists(self.file_name):
            self.conn = sqlite3.connect(self.file_name)
        else:
            self.create_table()
            self.conn = sqlite3.connect(self.file_name)

    def finalize(self):
        if self.conn is not None:
            self.conn.commit()
            self.conn.close()
            self.conn = None

    def create_table(self):
        conn = sqlite3.connect(self.file_name)
        conn.execute("""create table post
                     (url text primary key, title text, content text)""")
        conn.commit()
        conn.close()

    def process_item(self, item, spider):
        try:
            self.conn.execute('insert into post values(?,?,?)',
                              (item['url'], item['title'], item['content']))
        except Exception, e:
            print 'Failed to insert item: ' + item['url'] + "; Since:" + e
        return item