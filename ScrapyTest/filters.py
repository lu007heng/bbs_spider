import sqlite3

from scrapy.dupefilter import RFPDupeFilter

import settings

class DuplicateUrlFilter(RFPDupeFilter):

    def __init__(self, path=None, debug=False):
        self.url_seen = set()
        # load all the urls in db into memory
        conn = sqlite3.connect(settings.DATABASE['path'])
        cursor = conn.cursor()
        cursor.execute('''select url from post''')
        all_urls = cursor.fetchall()
        for url in all_urls:
            self.url_seen.add(url)
        RFPDupeFilter.__init__(self, path, debug)

    def request_seen(self, request):
        if request.url in self.url_seen:
            return True
        else:
            self.url_seen.add(request.url)
