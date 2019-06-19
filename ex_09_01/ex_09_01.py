counts = dict()
names = ["기모","기모","리나","리나"]


for name in names :
    counts[name] = counts.get(name,0) + 1

# GET 함수를 사용하면 아래 4줄을 위 한줄로 요약가능
#    if name not in counts :
#        counts[name] = 1
#    else :
#        counts[name] = counts[name] + 1


while True :
    newname = input ("newname == ")

    if newname == "done" :
        break

    elif newname == "list" :
        print("중간Dic집계", counts)

    elif newname not in counts :
        counts[newname] = 1
        names.append(newname)

    else :
        counts[newname] = counts[newname] + 1
        names.append(newname)


print ("최종Dic집계",counts)
