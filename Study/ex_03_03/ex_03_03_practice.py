

#내생일 2월 10일

while Ture :


scr = input ("오늘은 2월 몇일?: ")

try :
        fls = int(scr)
        if fls > int(10) :
            over = int (fls - 10)
        else :
            left = int (10-fls)
except :
        print ("숫자만 입력하세요")
        quit()

if fls > int(31) :
    print ("유효한 날짜가 아닙니다")

elif fls > int(10) :
    print ("생일",over,"일 초과")
    ask = input ("생일 챙겼어요? 네/아니오로 응답: ")
    if ask == str ("네") :
        print ("행복해요")
    else :
        print ("지옥의 시작")

elif fls == int(10) :
    print ("생일이에요 뿌우")
elif fls > int(7) :
    print ("긴급, 생일이",left,"밖에 남지 않았어요ㄷㄷ")
elif fls > int(4) :
    print ("생일준비모드",left,"정도 남았네")
elif fls > int(1) :
    print ("생일",left,"전")
