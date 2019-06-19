
count = 0
sumnumber = 0
emptylist = []

while True :

    new = input("숫자를 넣어라=> ")

    if new == "done" :
        break

    try :
        newnumber = int(new)
        sumnumber = sumnumber + newnumber
        emptylist.append(newnumber)
        count = count + 1
        continue

    except :
        print("숫자만 입력하세요")
        continue

list.sort(emptylist)
print ("list", emptylist)
print ("sum", sumnumber)
print ("개수count", count)
print ("리스트 원소count", len(emptylist))
