
numlist = []

while True :
    inp = input("숫자를 입력하세요")

    if inp == 'done' :
        break
    elif inp == 'print' :
        print(numlist)
    elif inp == 'len' :
        print(len(numlist))
    elif inp == 'sum' :
        print(sum(numlist))
    elif inp == 'max' :
        print(max(numlist))
    elif inp == 'min' :
        print(min(numlist))
    elif inp == 'avr' :
        print(sum(numlist)/len(numlist))
    elif inp == 'sort' :
        numlist.sort()
        print(numlist)
    else :
        value = float(inp)
        numlist.append(value)

average = sum(numlist)/len(numlist)
print("Average",average)
