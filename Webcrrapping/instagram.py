from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib.request
import time


insta_url = 'https://www.instagram.com'
insta_tag_url='https://www.instagram.com/explore/tags/'
insta_id = 'hjyu1408@gmail.com'
insta_pw = '14234yhj'
insta_tag = '강아지/'



###instagram_main
driver = wd.Chrome(executable_path='/usr/local/bin/chromedriver')
driver.get(insta_url)
driver.implicitly_wait(5)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[2]/p/a').click()



###instagram_login

    #1. 키 입력
time.sleep(3)
driver.find_elements_by_css_selector('form input')[0].send_keys(insta_id)
driver.find_elements_by_css_selector('form input')[1].send_keys(insta_pw)

    #2. 로그인 클릭
driver.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(4) > button').click()



###Notification 받지 않기 팝업창 클릭
driver.implicitly_wait(2)
driver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm').click()



#태그 검색하기


    #####서치바를 찾아 / 태그를 입력하고 / 엔터치는 방법 계속 오류...
# search_box= driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div')
# search_box.click().send_keys(insta_tag).send_keys(Keys.RETURN)

    # #로그인 된 창에서, 태그명이 아예 입력된 url 리로드하는 방법으로 진행
driver.get(insta_tag_url+insta_tag)



#이미지 긁어오기


    #1. 사진페이지 중 상단 인기사진 제외 / 하단 최근사진만 수집
most_recent= driver.find_element_by_css_selector('#react-root > section > main > article > div:nth-child(3) > div')
each_line = most_recent.find_element_by_class_name('Nnq7C weEfm')
each_picture = each_line.find_element_by_class_name('v1Nh3 kIKUG  _bz0w')

    # 2. 사진 수집하기
#우클릭을 해도 사진 저장불가 --> 사진의 개별 a태그를 저장하는 형태로 진행
#목표 사진URL 100개 리스트 수집

number = 0 
tag_list = []

for a_tag in each_picture:
    if a_tag.find_elements_by_tag_name('a'):
        number = number + 1
        tag = "https://www.instagram.com" + a_tag.find_elements_by_tag_name('a')
        tag_list.append(tag)
        driver.implicitly_wait(0.5)  #하단 사진들이 로딩되는 것을 기다리기 위해
        if number == 100:
            break    #100개가 쌓이면 코드 중단

print(tag_list)

     
