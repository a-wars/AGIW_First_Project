# -*- coding: utf-8 -*-

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class HiveSpider(CrawlSpider):
    name = 'hive'
    allowed_domains = ['www.hive.co.uk']
    start_urls = ['http://www.hive.co.uk/']
    rules = [Rule(LinkExtractor(), callback='parse_item', follow=True)]

    def parse_item(self, response):
        refererUrl = response.request.headers.get('Referer',None).decode("utf-8") 
        yield {
                "url": response.url,
                "referer_url": refererUrl,
                "src": response.text
        }