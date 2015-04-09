__author__ = 'Ron'

import sqlite3
from scrapy import log
from scrapy.exceptions import IgnoreRequest
import settings


class IgnoreDuplicates():

    def __init__(self):
        self.crawled_urls = set()

        with sqlite3.connect(settings.DATABASE['path']) as conn:
            cur = conn.cursor()
            cur.execute("""SELECT url FROM post""")
            self.crawled_urls.update(x[0] for x in cur.fetchall())

    def process_request(self, request, spider):
        if request.url in self.crawled_urls:
            log.msg('ignore duplicate url'+request.url, level=log.INFO)
            raise IgnoreRequest()
        else:
            return None