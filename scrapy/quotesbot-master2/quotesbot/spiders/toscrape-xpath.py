# -*- coding: utf-8 -*-
import scrapy
import pymongo

class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'toscrape-xpath_new'
    start_urls = [
        'http://quotes.toscrape.com/',
    ]

###Text, Author, Tag를 받아오는 코드
    def parse_page1(self, response):
        item = QuotesbotItem()

        for quote in response.start_urls:       
            item['text'] = quote.xpath('./span[@class="text"]/text()').extract()[0]
            item['author'] = quote.xpath('.//small[@class="author"]/text()').extract()[0]
            item['tags'] = quote.xpath('.//div[@class="tags"]/a[@class="tag"]/text()').extract()[0]
            
            request = scrapy.Request(quote.xpath('.//a/@href').extract()[0],callback=self.parse_page2)

            yield request


#Author > 더보기에 접속해서 받아오는 코드
    def parse_page2(self, response):
        item = QuotesbotItem()

        item['author_name'] = quote.xpath('./html/body/div/div[2]/h3/text()').extract()[0]
        item['author_born'] = quote.xpath('./html/body/div/div[2]/p[1]/span[1]/text()').extract()[0]
        item['author_description'] = quote.xpath('/html/body/div/div[2]/div/text()').extract()[0]
            
        yield item



#이건 어떻게 처리해야할지...
        # next_page_url = response.xpath('//li[@class="next"]/a/@href').extract_first()
        # if next_page_url is not None:
        #     yield scrapy.Request(response.urljoin(next_page_url))

