import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error

#comment 개수구하기
xml = urllib.request.urlopen('http://python-data.dr-chuck.net/comments_42.xml').read()
tree = ET.fromstring(xml)
lst = tree.findall('comments/comment')
print('Comment개수:', len(lst))


#count 더하기
numbers = list()
for item in lst :
    number = item.find('count').text
    numbers.append(int(number))
print('Number총합:',sum(numbers))
