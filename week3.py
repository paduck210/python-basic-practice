from urllib.request import urlopen
import urllib.error
import json
import sqlite3
import ssl

search_text = input("Type what you want to search: ")
data = urllib.request.urlopen('http://api.plos.org/search?q=title:'+search_text).read()


conn = sqlite3.connect('week3.sqlite')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS docs')
cur.execute('''CREATE TABLE docs
(id TEXT, journal TEXT, eissn TEXT, publication_date TEXT,
article_type TEXT,abstract TEXT, author_display TEXT, title_display TEXT, score FLOAT)''' )

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

js = json.loads(data)

first = js["response"]
second = first["docs"]

for each in second:
    newid = each["id"]
    newjl = each["journal"]
    newen = each["eissn"]
    newpu = each["publication_date"]
    newar = each["article_type"]
    newat = “,“.join(each[“author_display”])
    newab = “,“.join(each[“abstract”])   
    newti = each["title_display"]
    newsc = each["score"]


    cur.execute('''INSERT INTO docs (id, journal, eissn, publication_date, article_type, author_display, abstract, title_display, score)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', (newid,newjl,newen,newpu,newar,newat, newab,newti,newsc))
    conn.commit()

cur.close()
