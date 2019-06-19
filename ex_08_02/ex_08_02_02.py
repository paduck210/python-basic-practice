

#WHile loop를 통한 덧셈
count = 0
index = 0
while True :
    number = input ("Put user number asshole: ")
    if number == "done" :
        break
    inp = float(number)
    index = index + inp
    count = count + 1

print("합계",index)
print("평균",index/count)



#새로 배운 List를 활용한 덧셈
numberlist = list()
while True :
    number = input("Put ur number bitch: ")
    if number == "done" :
        break
    ipp = float(number)
    numberlist.append(ipp)


print("리스트", numberlist)
print("합계", sum(numberlist))
print("원소수", len(numberlist))
print("평균값", sum(numberlist)/len(numberlist))
