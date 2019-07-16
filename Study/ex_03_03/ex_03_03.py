scr = input ("Enter score: ")

try :
        fls = float(scr)
except :
        print ("숫자가 아니무니다")
        quit()

if fls > float(1.0) :
    print ("소숫점이 아니무니다")
elif fls >= float(0.9) :
    print ("A")
elif fls >= float(0.8) :
    print ("B")
elif fls >= float(0.7) :
    print ("C")
elif fls < float(0.6) :
    print ("F")
else :
    print ("헛소리 노노")
