__author__ = 'Ron'

import sqlite3
from scrapy.exceptions import IgnoreRequest


class IgnoreDuplicates():

    def __init__(self):
        self.crawled_urls = set()

        with sqlite3.connect('data.sqlite') as conn:
            cur = conn.cursor()
            cur.execute("""SELECT url FROM post""")
            self.crawled_urls.update(x[0] for x in cur.fetchall())

    def process_request(self, request, spider):
        if request.url in self.crawled_urls:
            raise IgnoreRequest()
        else:
            return None