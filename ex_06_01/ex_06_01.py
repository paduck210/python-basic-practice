
#문자열
fruit = "banana"
letter_first = fruit[0]
letter_second = fruit[1]
print(letter_first)
print(letter_second)


#sting 텍스트 열은 한글자씩 출력되는 엘리베이터 같은 개념
fruit = "banana"
index = 0
while index < len(fruit) :
    letter = fruit[index]
    print (index, letter)
    index = index + 1


#별도의 특수한 값에 대한 출력/조건을 원하는게 아니라
#순서대로 출력되는 것을 원하는 것이라면
#for 문이 while 문 보다 낫습니다

apple = "pineapple"
for letter in apple :
    print (letter)


#특정한 내가 찾는 값이 존재하는가
word = "기모르디테기모르디테기모기모르디테"
count = 0
counta = 0
for letter in word :
    if letter == '기' :
        count = "기모가 있아"

    elif letter == "기모" :
        counta = "기모가 있어"

print (count) #답은 기모가 있어로 출력
print (counta) #[기모]가 있어는 찾지 못한다


print ("="*10)

for letter in "banana" :
    print (letter)


print ("="*10)


for letter in "원석아 사랑해" :
    print (letter)



print ("="*10)

for letter in "123" :
    for carrot in "123" :
        print ("str=",letter,carrot,letter+carrot)
        print ("int=",int(letter),int(carrot),int(letter)+int(carrot))
