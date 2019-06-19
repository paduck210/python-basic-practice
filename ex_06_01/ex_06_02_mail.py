


info = "jung.yu@klook.com  010-2809-1408  유현정"


#메일주소 찾기
mail = info.find("@")
print(mail)

office = info.find(" ",mail)
print(office)

full = info[mail+1 : office]
print(full)


#번호찾기
number = info.find("010")
print(number)

phone = info.find(" ",number)
print(phone)

fullnum = info[number : phone]
print(fullnum)


#반복문단 단위로 원소 쪼개기 = split
info = "jung.yu@klook.com,010-2809-1408,유현정"
a = info.split(",")
print(a)
# >>['jung.yu@klook.com', '010-2809-1408', '유현정']


#메일주소 찾기 = 원소값 중 0번을 가져와
mail = a[0]
print(mail)
# >> jung.yu@klook.com


#원소 [a,b,c]로 쪼개져있는 것을 쪼갬단위를 넣어서 다시 합쳐라 = join
info2 = " | ".join(a)
print(info2)
# >> jung.yu@klook.com | 010-2809-1408 | 유현정
