import time
from selenium import webdriver
import xlrd
from xlutils.copy import copy
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException
import os


# driver로 wiki 접속
driver = webdriver.Chrome(executable_path="C:/Users\yunhwan\workspace\crazy\chromedriver.exe")

for i in range(1,101):
    driver.get("https://google.com")

    # 엑셀 파일 열기
    wb = xlrd.open_workbook('test.xls')
    sheet = wb.sheet_by_index(0)

    copy_wb = copy(wb)
    copy_sheet = copy_wb.get_sheet(0)


    # 검색 키워드 셀에서 가져오기
    song = sheet.cell(i, 1).value
    artist = sheet.cell(i, 2).value
    keyword = str(song) + ' ' + str(artist) #숫자인 경우가 있어서 str()

    #구글 검색
    elem = driver.find_element_by_id('lst-ib')

    #공통
    elem.send_keys(keyword)
    elem.submit()

    ##### 구글 검색 결과 페이지 #####
    try:
        box = driver.find_element_by_xpath("//div[@id='rso']/div[2]/div")
        list = box.find_elements_by_tag_name('h3')
        for item in list :
         #print(item.text)
            if( 'Wikipedia' in item.text ):
                p = item.find_element_by_tag_name('a')
                p.click()
                break


    except NoSuchElementException:
    
        box = driver.find_element_by_xpath("//div[@id='rso']/div/div")
        list = box.find_elements_by_tag_name('h3')
        for item in list:
            # print(item.text)
            if ('Wikipedia' in item.text):
                p = item.find_element_by_tag_name('a')
                p.click()
                break


    ##### 위키 곡정보 페이지  #####
    # writer,producer 
    print("//////////////////////////// " + str(i) + "행을 크롤링중입니다.")
    print("//////////////////////////// " + "노래명, 가수 : " + keyword)

    try:
        table = driver.find_element_by_tag_name('table')
        tbody = table.find_element_by_tag_name("tbody")
        trs = tbody.find_elements_by_tag_name("tr")
    
    except NoSuchElementException:
        print(" [예외 발생] 표 없음 ")
        continue


    for tr in trs:
       
        if "Writer(s)" in tr.text:
            print(tr.text)
            a = ""
            if tr.find_elements_by_tag_name("li"):
                lis = tr.find_elements_by_tag_name("li")
                for li in lis:
                    a = a + "," + li.text
            else:
                o = tr.find_elements_by_tag_name("td")
                a = a + "," + o[0].text

            a = a[1:]
            copy_sheet.write(i, 3, a)

        if "Producer" in tr.text:
            print(tr.text)
            a = ""
            if tr.find_elements_by_tag_name("li"):
                lis = tr.find_elements_by_tag_name("li")
                for li in lis:
                    a = a + "," + li.text
            else:
                o = tr.find_elements_by_tag_name("td")
                a = a + "," + o[0].text

            a = a[1:]
            copy_sheet.write(i, 4, a)


    #저장
    copy_wb.save('test.xls')