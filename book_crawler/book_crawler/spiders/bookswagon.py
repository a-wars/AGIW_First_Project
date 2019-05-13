# -*- coding: utf-8 -*-

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class BookswagonSpider(CrawlSpider):
    name = 'bookswagon'
    allowed_domains = ['www.bookswagon.com']
    start_urls = ['http://www.bookswagon.com/']
    rules = [Rule(LinkExtractor(), callback='parse_item', follow=True)]

    def parse_item(self, response):
        refererUrl = response.request.headers.get('Referer',None).decode("utf-8") 
        yield {
                "url": response.url,
                "referer_url": refererUrl,
                "src": response.text
        }