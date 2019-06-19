import xml.etree.ElemneTree as ET
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

html = urllib.request.urlopen('http://python-data.dr-chuck.net/comments_42.xml', context=ctx).read()
#soup = BeautifulSoup(html, 'html.parser')

tree = ET.fromstring(html)
print('count',tree.find('count'),text)






#numbers = list()
#for span in spans:
#    number = re.findall('[0-9]+',span.string)
#    numbers = numbers + number

#renum = list()
#for each_num in numbers:
#    each_num = int(each_num)
#    renum.append(each_num)

#print("합계",sum(renum))
#print("개수",len(renum))
