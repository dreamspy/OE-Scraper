# -*- coding: utf-8 -*-
import scrapy

from oe.items import OeItem
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

class OpticseducationSpider(CrawlSpider):
    name = "opticseducation"
    allowed_domains = ["www.opticseducation.org"]
    start_urls = (
        'http://www.opticseducation.org/search.aspx?searchmode=anyword&searchstate=0&searchcountry=79&searchdisciplines=&searchdegree=&searchtuition=0&resident=',
    )
#    rules = [Rule(LinkExtractor(allow=['http://www.opticseducation.org/members/*']), callback='parse_link')]
    rules = [Rule(LinkExtractor(allow=['http://www.opticseducation.org/members/*']))]

    # def parse(self, response):
    #     filename = response.url.split("/")[-2]
    #     with open(filename, 'wb') as f:
    #         f.write(response.body)

    def parse(self, response):
    	pass
        for sel in response.xpath('//td/a'): #this works!
            item = OeItem()
            item['title'] = sel.xpath('text()').extract()[0].replace('\r\n','').strip()
            item['link'] = sel.xpath('@href').extract()[0].replace('\r\n','').strip()
            yield item

    def parse_link():
    	pass
		# item = OeItem()
		# item['title'] = sel.xpath('text()').extract()[0].replace('\r\n','').strip()
		# item['link'] = sel.xpath('@href').extract()[0].replace('\r\n','').strip()
		# return item








