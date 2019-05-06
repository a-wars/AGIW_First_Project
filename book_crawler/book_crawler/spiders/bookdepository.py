# -*- coding: utf-8 -*-

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class BookdepositorySpider(CrawlSpider):
    name = 'bookdepository'
    allowed_domains = ['www.bookdepository.com']
    start_urls = ['http://www.bookdepository.com/']
    rules = [Rule(LinkExtractor(), callback='parse_item', follow=True)]

    def parse_item(self, response):
        refererUrl = response.request.headers.get('Referer',None).decode("utf-8") 
        yield {
                "url": response.url,
                "referer_url": refererUrl,
                "src": response.text
        }