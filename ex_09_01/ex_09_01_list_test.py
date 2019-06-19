hello = list()

while True :

    a = input("Enter number== ")

    if a == "done" :
        break
    else :
        hello.append(int(a))

print ("입력된순서대로", hello)
print(hello[1])


print("정렬 가즈아")

hello.sort()

print ("정렬된순서대로",hello)
print(hello[1])
