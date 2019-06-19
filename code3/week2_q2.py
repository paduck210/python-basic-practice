# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl


#아래 3줄과 context=ctx 하나는 https에 접속하기 위한 방법
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# 여기부터가 배우는 코드
fhand = urllib.request.urlopen('http://onepound.kr/', context=ctx).read()
soup = BeautifulSoup(fhand, 'html.parser')
#beautifulsoup4가 utf-8, 유니코드를 읽을 수 있음

# Retrieve all of the anchor tags
tags = soup('tr')
for tag in tags:
    print(tag.get('td', None))
