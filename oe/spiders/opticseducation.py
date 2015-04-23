# -*- coding: utf-8 -*-
import scrapy

from oe.items import OeItem

class OpticseducationSpider(scrapy.Spider):
    name = "opticseducation"
    allowed_domains = ["www.opticseducation.org"]
    start_urls = (
        'http://www.opticseducation.org/search.aspx?searchmode=anyword&searchstate=0&searchcountry=79&searchdisciplines=&searchdegree=&searchtuition=0&resident=',
    )

    # def parse(self, response):
    #     filename = response.url.split("/")[-2]
    #     with open(filename, 'wb') as f:
    #         f.write(response.body)

    def parse(self, response):
        for sel in response.xpath('//td/a'): #this works!
            item = OeItem()
            item['title'] = sel.xpath('text()').extract()
            item['link'] = sel.xpath('@href').extract()
            yield item