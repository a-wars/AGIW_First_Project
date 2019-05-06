# -*- coding: utf-8 -*-

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup
import re

bookRegex =  r'^https\:\/\/www\.ibs\.it\/libri(\/|$)'

class IbsSpider(CrawlSpider):
    name = 'ibs'
    allowed_domains = ['ibs.it']
    start_urls = ['http://ibs.it/']
    rules = [Rule(LinkExtractor(), callback='parse_item', follow=True)]

    def parse_item(self, response):
        pageURL = response.url
        print("pageURL is ")
        print(pageURL)
        refererURL = response.request.headers.get('Referer',None).decode("utf-8") 
        print("refererURL is ")
        print(refererURL)
        body = BeautifulSoup(response.body,'html.parser').body
        if re.match(bookRegex, pageURL) or re.match(bookRegex, refererURL):
            yield {
                "url": pageURL,
                "referring_url": refererURL,
                "src": str(body)
            }