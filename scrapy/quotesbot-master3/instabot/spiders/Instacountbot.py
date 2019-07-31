# -*- coding: utf-8 -*-
import scrapy
from instabot.items import InstaTagCount
import time
import json
from datetime import datetime
import getpass
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
#from webdriver_manager.chrome import ChromeDriverManager as wd

# driver = webdriver.Chrome(r"C:/Users/paduck/Downloads/chromedriver_mac64/chromedriver.exe")

class ToScrapeInstaXPath(scrapy.Spider):
    name = 'instacountbot'
    start_urls = [
        'https://www.instagram.com/accounts/login/?source=auth_switcher' ,
    ]
    tag_search_url = 'https://www.instagram.com/explore/tags/'
    insta_id = input('jung210_a')
    insta_pw = getpass.getpass('14234yhj')
    keyword  = input('montreal')

    def __init__(self):
        scrapy.Spider.__init__(self)
        self.browser = wd.Chrome()
#        self.browser = wd.Chrome(executable_path='./chromedriver')

    def parse(self, response):

        #log in to instagram
        self.browser.get(response.url)
        self.browser.implicitly_wait(10)
        self.browser.find_element_by_xpath("//*").get_attribute('outerHTML')
        time.sleep(10)
        self.browser.find_elements_by_css_selector('form input')[0].send_keys(insta_id)
        self.browser.find_elements_by_css_selector('form input')[1].send_keys(insta_pw)
        time.sleep(10)
        self.browser.find_elements_by_css_selector('form input')[1].send_keys(Keys.ENTER)
        time.sleep(10)
        self.browser.find_element_by_css_selector('form button').click()

        #reload tag url
        tag_search_url = tag_search_url + keyword
        time.sleep(10)
        self.browser.get(tag_search_url)

        # I'm not a robot
        time.sleep(10)

        # collect count number
        item = InstaTagCount()
        date = str(datetime.now())
        item['tag_name'] = quote.xpath('//*[@id="react-root"]/section/main/header/div[2]/div[1]/h1/text()').extract()[0],
        item['tag_count']= quote.xpath('//*[@id="react-root"]/section/main/header/div[2]/div[2]/span/span').extract()[0],
        item['tag_date'] = date[0:10]
        yield item
