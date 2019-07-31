from selenium import webdriver as wd
import time
import scrapy
import json

class LifeSpider(scrapy.Spider):
    name = "seleniumHybrid.py"
    start_urls = [
        'https://www.brainyquote.com/topics/life',
    ]

    def __init__(self):
        # init browser with Selenium chrome driver here
        scrapy.Spider.__init__(self)
        self.browser = wd.Chrome(executable_path='./chromedriver')

    def parse(self, response):
        # load page on Selenium then wait for full-loading
        self.browser.get(response.url)
        self.browser.implicitly_wait(5)

        # prepare for infinite scrolling limit to 500 results
        seen = set()
        LIMIT_OF_RESULTS = 100

        # Get scroll height
        last_height = self.browser.execute_script("return document.body.scrollHeight")
        print('last height:', last_height)

        while len(seen) < LIMIT_OF_RESULTS:
            # parse html page to select with xpath
            html = self.browser.find_element_by_xpath("//*").get_attribute('outerHTML')
            selector = scrapy.Selector(text=html)

            # collect quotes
            for quote in selector.xpath('//*[@id="quotesList"]/div[starts-with(@id, "qpos")]'):
                text = quote.xpath('div[1]/div/a[1]/text()')[0].extract()
                author = quote.xpath('div[1]/div/a[2]/text()')[0].extract()
                tags = quote.xpath('div[2]/a/text()').extract()

                if text not in seen:
                    seen.add(text)
                    yield {
                        'text': text,
                        'author': author,
                        'tags': tags
                    }

            # scroll down to bottom
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(3)

            # Calculate new scroll height and compare with last scroll height
            new_height = self.browser.execute_script("return document.body.scrollHeight")
            print('new height:', new_height, 'last height:', last_height)
            if new_height == last_height:
                print("the end of document")
                break
            last_height = new_height

            print("seen : ", len(seen))
