from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen('http://python-data.dr-chuck.net/comments_42.html')
source = html.read()

html.close()

print(source)
