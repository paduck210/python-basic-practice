aa = input("정수a입력")
bb = input ("정수b입력")


try :
    a = int(aa)
    b = int(bb)

except :
        print("숫자를 입력하세요")
        quit ()


def max_double(a, b) :
    return max(a, b) * 2

print(max_double(a,b))
