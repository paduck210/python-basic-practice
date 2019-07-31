# -*- coding: utf-8 -*-
import scrapy
from quotesbot.items import QuoteItem, AuthorItem
from selenium import webdriver as wd
import time
import json
from datetime import datetime


class ToScrapeInstaXPath(scrapy.Spider):
    name = 'instacountCrawler'
    start_urls = [
        'https://www.instagram.com/accounts/login/?source=auth_switcher' ,
    ]
    tag_search_url = 'https://www.instagram.com/explore/tags/'
    insta_id = input('jung210_a')
    insta_pw = getpass.getpass('password')
    keyword  = input('montreal')

    def __init__(self):
        scrapy.Spider.__init__(self)
        self.browser = wd.Chrome(executable_path='./chromedriver')

    def parse(self, response):

        #log in to instagram
        self.browser.get(response.url)
        self.browser.implicitly_wait(5)
        self.browser.find_element_by_xpath("//*").get_attribute('outerHTML')
        time.sleep(2)
        self.browser.find_elements_by_css_selector('form input')[0].send_keys(insta_id)
        self.browser.find_elements_by_css_selector('form input')[1].send_keys(insta_pw)
        self.browser.find_elements_by_css_selector('form input')[1].send_keys(Keys.ENTER)
        self.browser.find_element_by_css_selector('form button').click()

        #reload tag url
        tag_search_url = tag_search_url + keyword
        self.browser.get(tag_search_url)

        # I'm not a robot
        time.sleep(2)

        # collect count number
        item['tag_name'] = quote.xpath('//*[@id="react-root"]/section/main/header/div[2]/div[1]/h1/text()').extract()[0]
        item['tag_count'] = quote.xpath('//*[@id="react-root"]/section/main/header/div[2]/div[2]/span/span').extract()[0]
        date = str(datetime.now())
        item['tag_date'] = a[0:10]
        yield request



