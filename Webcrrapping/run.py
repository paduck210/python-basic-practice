#인터파크 여행 사이트에서 여행지를 입력 후 검색
#로그인 시 PC사이트에서 처리가 어려울 경우 -> 모바일 페이지로 이동

from selenium import webdriver as wd

#For Explicit wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#사전에 필요한 정보를 로드 #디비, 쉘, 파일에서 인지받기 
main_url = 'http://tour.interpark.com/'
keyword = '로마'

#드라이버 로드 
driver = wd.Chrome(executable_path='/usr/local/bin/chromedriver')
#차후 옵션부여하여 /프록시, 에이전트 조작, 이미지 배제
#크롤링을 오래 돌리면 임시 파일들이 쌓인다 > 템포 파일 삭제 필요 

#사이트 접속 (get)
driver.get(main_url)

#검색창을 찾아 + 검색어를 입력
#id: SearchGNBText
driver.find_element_by_id('SearchGNBText').send_keys(keyword)
#tip. 수정할 경우 = > 뒤에 내용이 붙어버림  => .clear() -> send.keys('내용)
#검색버튼을 클릭
driver.find_element_by_css_selector('button.search-btn').click()
#잠시 대기 -> 페이지 로드 후 즉시 테이터를 획득하는 행위는 지양 
#https://selenium-python.readthedocs.io/waits.html#
#Explicit wait -> till. find element 
try:
    element= WebDriverWait(driver, 10).until(
         #지정한 한개 요소가 올라오면 wait를 종료하겠다
         EC.presence_of_element_located((By.CLASS_NAME, 'oTravelBox'))
    )
except Exception as e:
    print('오류 발생',e)

#암묵적 대기 => Dom이 다 로드 될때까지 대기하고 먼저 로드되면 바로 진행
#요소를 찾을 특정 시간 동안 DOM 풀링을 지시 ex. 10초 이내라도 발견되면 바로 진행
driver.implicitly_wait(10)
#implicit wait -> time.sleep(10) -> cloud pair(defence DDOS)

#더보기 눌러서 게시판 진입
#driver.find_element_by_css_selector('.oTravelBox>.boxList>.moreBtnWrap>.moreBtn').click()
driver.find_element_by_css_selector('body > div.container > div > div > div.panelZone > div.oTravelBox > ul > li.moreBtnWrap > button').click()

###################################################################
#여러 사이트에서 정보를 수집할 경우 공통 정보 정의 단계 필요
#상품명 뽑기 = http://search-tour.interpark.com/PC/Result?search=%EB%A1%9C%EB%A7%88&code1=R&code2=


# 10번쨰 상품 테이블이 열릴때까지 대기
def find(driver):
    element = driver.find_elements_by_css_sector("li:nth-child(10)")
    if element:
        return element
    else:
        return False



#상품명 읽기 = 총 10개
boxItems = driver.find_elements_by_css_selector('body > div.container > div > div > div.panelZone > div.oTravelBox > ul > li')
for li in boxItems:
    print( '상품명==', li.find_element_by_css_selector('h5').text )
    print( '코멘트==', li.find_element_by_css_selector('h5').text )
    print( '상품명==', li.find_element_by_css_selector('h5').text )
    