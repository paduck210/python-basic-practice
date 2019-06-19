sh = input("Enter Hours: ")
sr = input("Enter Rate: ")

try:
    fh = float(sh)
    fr = float(sr)
except:
    print("Erro,please enter numeric input")
    quit ()

print (fh,fr)


if fh >= 40 :
    #print ("Overtime")
    reg = fh * fr
    ovp = (fh - 40.0) * (fr * 0.5)
    xp = reg + ovp
else :
    xp = fh * fr
print ("Pay",xp)
