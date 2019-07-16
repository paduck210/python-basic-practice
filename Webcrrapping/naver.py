from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

naver_url = 'https://nid.naver.com/nidlogin.login'
naver_id = 'paduck210'
naver_pw = '14234yhj!'



browser = wd.Chrome("/usr/local/bin/chromedriver")
browser.get(naver_url)

id = browser.find_element_by_css_selector('#id').send_keys(naver_id)
pw = browser.find_element_by_xpath('//*[@id="pw"]').send_keys(naver_pw)

browser.find_element_by_css_selector('#frmNIDLogin > fieldset > input').click()
