import json
import urllib.request, urllib.parse, urllib.error

data = urllib.request.urlopen('http://python-data.dr-chuck.net/comments_353540.json').read()
info = json.loads(data)


#http://python-data.dr-chuck.net/comments_353540.json


#json 자료가 딕셔너리 안에 리스트 note, comment가 위치
#이를 알아보기 위해 예전에 배웠던 딕셔너리 ket값만 추출하는 함수 사용
#info.key()
#결과 note, comments

#info["comment"]를 지정하여 원하는 리스트만 추철하여 이후 작업 진행


#comment 개수세기
namelist = list()
for item in info["comments"] :
    name = item['name']
    namelist.append(name)
print("Comment 개수", len(namelist))


#number 더하기
numlist = list()
for items in info["comments"] :
    number = item["count"]
    numlist.append(number)
print("Num 합산", sum(numlist))
