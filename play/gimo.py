



print ("다음 중 [기모르디테]는 몇번 나올까요?")

print ("="*40)

gimo = ("기기기모모모갓기모모기모르디테모모기기기기기기기기기모모기모르디테모모모기기여신모모모모모기기기기기모르디테기기기기기"*10)
a = print(gimo)

#정답
#print(gimo.count('기모르디테'))
#30
print ("="*40)

while True :

    answer = input ("정답을 입력하세요: ")

    try :
        value = int(answer)


    except :
        print ("정수만 입력해 멍청아")
        continue


    if value > 30 :
        print ("Down")
        continue

    elif value < 30 :
        print ("UP")
        continue

    elif value == 30 :
        break



print ("짝짝짝 정답!!!")
