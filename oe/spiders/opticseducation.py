# -*- coding: utf-8 -*-
# import scrapy

from oe.items import OeItem
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor


class OpticseducationSpider(CrawlSpider):
    name = "opticseducation"
    allowed_domains = ["www.opticseducation.org"]
    # start_urls = (
    #     'http://www.opticseducation.org/search.aspx?searchmode=anyword&searchstate=0&searchcountry=235&searchdisciplines=&searchdegree=&searchtuition=0&resident=0&page=1',
    # )

    start_urls = (
		"http://www.opticseducation.org/search.aspx?searchmode=anyword&searchstate=0&searchcountry=0&searchdisciplines=7&searchdegree=&searchtuition=0&resident=0&page=1",
		"http://www.opticseducation.org/search.aspx?searchmode=anyword&searchstate=0&searchcountry=0&searchdisciplines=7&searchdegree=&searchtuition=0&resident=0&page=2",
		"http://www.opticseducation.org/search.aspx?searchmode=anyword&searchstate=0&searchcountry=0&searchdisciplines=7&searchdegree=&searchtuition=0&resident=0&page=3",
		"http://www.opticseducation.org/search.aspx?searchmode=anyword&searchstate=0&searchcountry=0&searchdisciplines=7&searchdegree=&searchtuition=0&resident=0&page=4",
		"http://www.opticseducation.org/search.aspx?searchmode=anyword&searchstate=0&searchcountry=0&searchdisciplines=7&searchdegree=&searchtuition=0&resident=0&page=5",
		"http://www.opticseducation.org/search.aspx?searchmode=anyword&searchstate=0&searchcountry=0&searchdisciplines=7&searchdegree=&searchtuition=0&resident=0&page=6",
		"http://www.opticseducation.org/search.aspx?searchmode=anyword&searchstate=0&searchcountry=0&searchdisciplines=7&searchdegree=&searchtuition=0&resident=0&page=7",
		"http://www.opticseducation.org/search.aspx?searchmode=anyword&searchstate=0&searchcountry=0&searchdisciplines=7&searchdegree=&searchtuition=0&resident=0&page=8",
		"http://www.opticseducation.org/search.aspx?searchmode=anyword&searchstate=0&searchcountry=0&searchdisciplines=7&searchdegree=&searchtuition=0&resident=0&page=9",
		"http://www.opticseducation.org/search.aspx?searchmode=anyword&searchstate=0&searchcountry=0&searchdisciplines=7&searchdegree=&searchtuition=0&resident=0&page=10",
		"http://www.opticseducation.org/search.aspx?searchmode=anyword&searchstate=0&searchcountry=0&searchdisciplines=7&searchdegree=&searchtuition=0&resident=0&page=11",
		"http://www.opticseducation.org/search.aspx?searchmode=anyword&searchstate=0&searchcountry=0&searchdisciplines=7&searchdegree=&searchtuition=0&resident=0&page=12",
		"http://www.opticseducation.org/search.aspx?searchmode=anyword&searchstate=0&searchcountry=0&searchdisciplines=7&searchdegree=&searchtuition=0&resident=0&page=13",
		"http://www.opticseducation.org/search.aspx?searchmode=anyword&searchstate=0&searchcountry=0&searchdisciplines=7&searchdegree=&searchtuition=0&resident=0&page=14",
		"http://www.opticseducation.org/search.aspx?searchmode=anyword&searchstate=0&searchcountry=0&searchdisciplines=7&searchdegree=&searchtuition=0&resident=0&page=15",
		"http://www.opticseducation.org/search.aspx?searchmode=anyword&searchstate=0&searchcountry=0&searchdisciplines=7&searchdegree=&searchtuition=0&resident=0&page=16",
		"http://www.opticseducation.org/search.aspx?searchmode=anyword&searchstate=0&searchcountry=0&searchdisciplines=7&searchdegree=&searchtuition=0&resident=0&page=17",
		"http://www.opticseducation.org/search.aspx?searchmode=anyword&searchstate=0&searchcountry=0&searchdisciplines=7&searchdegree=&searchtuition=0&resident=0&page=18",
		"http://www.opticseducation.org/search.aspx?searchmode=anyword&searchstate=0&searchcountry=0&searchdisciplines=7&searchdegree=&searchtuition=0&resident=0&page=19",
		"http://www.opticseducation.org/search.aspx?searchmode=anyword&searchstate=0&searchcountry=0&searchdisciplines=7&searchdegree=&searchtuition=0&resident=0&page=20",
		"http://www.opticseducation.org/search.aspx?searchmode=anyword&searchstate=0&searchcountry=0&searchdisciplines=7&searchdegree=&searchtuition=0&resident=0&page=21",
		"http://www.opticseducation.org/search.aspx?searchmode=anyword&searchstate=0&searchcountry=0&searchdisciplines=7&searchdegree=&searchtuition=0&resident=0&page=22",
		"http://www.opticseducation.org/search.aspx?searchmode=anyword&searchstate=0&searchcountry=0&searchdisciplines=7&searchdegree=&searchtuition=0&resident=0&page=23",
		"http://www.opticseducation.org/search.aspx?searchmode=anyword&searchstate=0&searchcountry=0&searchdisciplines=7&searchdegree=&searchtuition=0&resident=0&page=24",
		"http://www.opticseducation.org/search.aspx?searchmode=anyword&searchstate=0&searchcountry=0&searchdisciplines=7&searchdegree=&searchtuition=0&resident=0&page=25",
		"http://www.opticseducation.org/search.aspx?searchmode=anyword&searchstate=0&searchcountry=0&searchdisciplines=7&searchdegree=&searchtuition=0&resident=0&page=26",
		"http://www.opticseducation.org/search.aspx?searchmode=anyword&searchstate=0&searchcountry=0&searchdisciplines=7&searchdegree=&searchtuition=0&resident=0&page=27",
		"http://www.opticseducation.org/search.aspx?searchmode=anyword&searchstate=0&searchcountry=0&searchdisciplines=7&searchdegree=&searchtuition=0&resident=0&page=28",
		"http://www.opticseducation.org/search.aspx?searchmode=anyword&searchstate=0&searchcountry=0&searchdisciplines=7&searchdegree=&searchtuition=0&resident=0&page=29",
		"http://www.opticseducation.org/search.aspx?searchmode=anyword&searchstate=0&searchcountry=0&searchdisciplines=7&searchdegree=&searchtuition=0&resident=0&page=30",
		"http://www.opticseducation.org/search.aspx?searchmode=anyword&searchstate=0&searchcountry=0&searchdisciplines=7&searchdegree=&searchtuition=0&resident=0&page=31",
		"http://www.opticseducation.org/search.aspx?searchmode=anyword&searchstate=0&searchcountry=0&searchdisciplines=7&searchdegree=&searchtuition=0&resident=0&page=32",
		"http://www.opticseducation.org/search.aspx?searchmode=anyword&searchstate=0&searchcountry=0&searchdisciplines=7&searchdegree=&searchtuition=0&resident=0&page=33",
		"http://www.opticseducation.org/search.aspx?searchmode=anyword&searchstate=0&searchcountry=0&searchdisciplines=7&searchdegree=&searchtuition=0&resident=0&page=34"
	)


    rules = [
        Rule(LinkExtractor(allow=['http://www.opticseducation.org/members/*']),'parse_link')
    ]


    def parsetest(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)

    def parse_link(self, response):
        # for sel in response.xpath('//td/a'): #this works!
        #     item['title'] = sel.xpath('text()').extract()[0].replace('\r\n','').strip()
        item = OeItem()
        item['school'] = response.xpath('//*[@class = "LabelField"]/text()').extract()[0].replace('\r\n','').strip()
        item['st_core'] = response.xpath('//*[@id="right-col"]/div/p[5]/text()').extract()[0].replace('\r\n','').strip()
        item['st_related'] = response.xpath('//*[@id="right-col"]/div/p[6]/text()').extract()[0].replace('\r\n','').strip()
        item['country'] = response.xpath('//*[@id="right-col"]/div/p[1]/text()').extract()[0].replace('\r\n','').strip()
        item['url'] = response.request.url
        item['year'] = response.xpath('//*[@id="right-col"]/div/p[17]/text()').extract()[0].replace('\r\n','').strip()
        yield item

