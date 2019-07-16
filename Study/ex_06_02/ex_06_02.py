
#찾기 = 참 거짓값으로 결과값 보기
fruit = "banana"
print('m' in fruit )
# >>False

#찾기 = 위치 확인하기
test = "apple"
steve = test.find("p")
print (steve)
# >> 1

#검색해서 바꾸기
test = "steve jobs"
testt = test.upper()
change = testt.replace("JOBS","paduck")
print(change)


#공백없애기
space = "   hello world   "

cleanall = space.strip()
print(cleanall)

cleanleft = space.lstrip()
print(cleanleft)

cleanright = space.rstrip()
print(cleanright)


#접두사
hello = "new zealand"
helloA = hello.startswith("new")
print (helloA)
#True

helloB = hello.startswith("n")
print (helloB)
#True

helloB = hello.startswith("N")
print (helloB)
#Flase
