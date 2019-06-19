sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
fh = float(sh)
fr = float(sr)
#print ("Hours=",fh,"Rate=",fr)
if fh >= 40 :
    #print ("Overtime")
    reg = fh * fr
    ovp = (fh - 40.0) * (fr * 0.5)
    #print ("보통급여=", reg,""추가시급=",ovp)
    xp = reg + ovp
else :
    #print ("Regular")
    xp = fh * fr
print ("Pay",xp)
