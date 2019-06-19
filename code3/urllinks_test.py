# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

html = urllib.request.urlopen('http://python-data.dr-chuck.net/comments_42.html', context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
spans = soup("span")

###############################

numbers = list()
for span in spans:
    number = re.findall('[0-9]+',span.string)
    numbers = numbers + number

renum = list()
for each_num in numbers:
    each_num = int(each_num)
    renum.append(each_num)

print("합계",sum(renum))
print("개수",len(renum))
