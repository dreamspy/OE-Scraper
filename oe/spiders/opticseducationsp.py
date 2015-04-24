# -*- coding: utf-8 -*-
import scrapy

from oe.items import OeItem
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor


class OpticseducationSpider(CrawlSpider):
    name = "opticseducationsp"
    allowed_domains = ["www.opticseducation.org"]
    start_urls = (
        'http://www.opticseducation.org/members/joachim.eichler@tu-berlin.de.aspx',
    )

    def parse(self, response):
        pass
        # for sel in response.xpath('//td/a'): #this works!
        item = OeItem()
        #     item['title'] = sel.xpath('text()').extract()[0].replace('\r\n','').strip()
        item['school'] = response.xpath('//*[@class = "LabelField"]/text()').extract()[0].replace('\r\n','').strip()
        item['nrofstudents'] = response.xpath('//*[@id="right-col"]/div/p[5]/text()').extract()[0].replace('\r\n','').strip()
        yield item

    def parse_link():
        pass
        # item = OeItem()
        # item['title'] = sel.xpath('text()').extract()[0].replace('\r\n','').strip()
        # item['link'] = sel.xpath('@href').extract()[0].replace('\r\n','').strip()
        # return item
