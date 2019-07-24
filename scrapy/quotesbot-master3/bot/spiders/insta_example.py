from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import time
import getpass
import xlsxwriter
from io import BytesIO
import urllib.request
from PIL import Image
import sys

# To start with login page in any case
login_url = 'https://www.instagram.com/accounts/login/?source=auth_switcher' 
# tag search url
tag_search_url = 'https://www.instagram.com/explore/tags/'

# take user's id, password and keyword
insta_id = input('Enter your Instagram id: ')
insta_pw = getpass.getpass('Instagram password: ')
keyword  = input('type the tag word you desire: ')

# webdriver (chrome)
# for mac
driver = wd.Chrome(executable_path='./chromedriver')
# for windows
# driver = wd.Chrome(executable_path='chromedriver.exe')
# for ghost
# driver = wd.PhantomJS(executable_path='./phantomjs')

# start connect to the login
driver.get(login_url)

# try to find id and password input 
try:
    # driver.find_element_by_id('f3c8f98333452c4').send_keys(insta_id)
    driver.find_elements_by_css_selector('form input')[0].send_keys(insta_id)
    driver.find_elements_by_css_selector('form input')[1].send_keys(insta_pw)

    # forcefully wait 2 seconds before submitting
    time.sleep(2)
    driver.find_elements_by_css_selector('form input')[1].send_keys(Keys.ENTER)
    # driver.find_element_by_css_selector('form button').click()

except NoSuchElementException as error:
    print('We need rebuilding the log-in part of code with reflecting follow messages:', error)

# I'm not a robot
time.sleep(2)

# enter new url to find images
tag_search_url = tag_search_url + keyword
driver.get(tag_search_url)

# I'm not a robot
time.sleep(2)

# define image link lists to limit to 100 results
image_link_list = []
seen = set()
LIMIT_OF_RESULTS = 100

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
print('last height:', last_height)

while len(image_link_list) < LIMIT_OF_RESULTS:
    # collect every images combined with img tag
    imgs = driver.find_elements_by_css_selector('img')
    print('the length of image list:', len(image_link_list))
    print('the length of imgs:', len(imgs))

    # collect image links
    for img in imgs:
        try: 
            src_img = img.get_attribute('src')
            # print(type(src_img), src_img)
            if src_img not in seen:
                seen.add(src_img)
                image_link_list.append(src_img)

        except StaleElementReferenceException as error:
            # I'm not sure why sometimes this error occurs to me. lol
            print('We need rebuilding the extracting image part of code with reflecting follow messages:', error)

    # scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(3)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    print('new height:', new_height, 'last height:', last_height)
    if new_height == last_height:
        print("the end of document")
        break
    last_height = new_height


print('total image links:', len(image_link_list))

# open new workbook and set up worksheet
workbook = xlsxwriter.Workbook('pictures.xlsx')
worksheet = workbook.add_worksheet()
CELL_WIDTH = 200
CELL_HEIGHT = 200
worksheet.set_default_row(CELL_HEIGHT)
worksheet.set_column(0, 0, CELL_WIDTH)
row_count = 1 # starting row number

for link in image_link_list:
    # print('link:', link)
    
    # Read an image from a remote url.
    image_data = BytesIO(urllib.request.urlopen(link).read())

    # get width and height from the loaded image
    image_pil = Image.open(image_data)
    width, height = image_pil.size

    x_scale = CELL_WIDTH / width # It seems like excel column width calculation is somewhat ambiguous
    y_scale = CELL_HEIGHT / height

    # Write the byte stream image to a cell. Note, the filename must be
    # specified. In this case it will be read from url string.
    row_number = 'A' + str(row_count)
    print('saving link to row:', row_number,'/',len(image_link_list))
    row_count += 1
    worksheet.insert_image(row_number, link, {'image_data': image_data, 'x_scale': x_scale, 'y_scale': y_scale})

# clean up excel workbook
workbook.close()

# terminate chrome browser
driver.close()
driver.quit()

# terminate python interpreter
sys.exit(0) # <- this is raising uncaught exception in Visual studio code 