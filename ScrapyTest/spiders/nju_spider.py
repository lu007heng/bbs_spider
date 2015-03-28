# coding=utf-8

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

from ScrapyTest.items import NjuPostItem


class NjuSpider(CrawlSpider):
    name = 'nju_spider'
    allowed_domains = ['bbs.nju.edu.cn']
    start_urls = ['http://bbs.nju.edu.cn/bbstdoc?board=WarAndPeace']
    rules = [Rule(LinkExtractor(allow=['bbstcon\?board=WarAndPeace&file=M\.\d+\.A']),
                  callback='parse_post'),
             Rule(LinkExtractor(allow=['bbstdoc\?board=WarAndPeace&start=\d+']),
                  follow=True)]

    def parse_post(self, response):
        # self.log('A response from %s just arrived!' % response.url)
        post = NjuPostItem()
        post['url'] = response.url
        post['title'] = 'to_do'
        post['content'] = 'to_do'
        return post