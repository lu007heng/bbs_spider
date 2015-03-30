# -*- coding: utf-8 -*-

# Scrapy settings for ScrapyTest project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'ScrapyTest'

SPIDER_MODULES = ['ScrapyTest.spiders']
NEWSPIDER_MODULE = 'ScrapyTest.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'ScrapyTest (+http://www.yourdomain.com)'

# DUPEFILTER_CLASS = 'ScrapyTest.filters.DuplicateUrlFilter'
# DUPEFILTER_DEBUG = True

ITEM_PIPELINES = {
    'ScrapyTest.pipelines.SQLitePipeline': 400,
}

DOWNLOADER_MIDDLEWARES = {
    'ScrapyTest.middlewares.IgnoreDuplicates': 543,
}

DOWNLOAD_DELAY = 2
