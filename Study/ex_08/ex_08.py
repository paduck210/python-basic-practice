han = open ('mbox-short.txt')

for line in han :

    line = line.rstrip()
#    print("line===",line)
    bro = line.split()
#    print("words===",bro)


#   공란일때 넘어가라 방법1 + 공란임을 명시하라
#    if line == "" :
#        print("blank")
#        continue

#    공란일떄 넘어가라 방법2 = 원소가 별로 없으면 그냥 넘어가라
#    if len(bro) < 3 :
#        continue

#   From 으로 시작되지 않는 것은 무시해라
#    if bro[0] != "From" :
#        print("ignore")
#        continue


#   만약, 원소수가 적거나 / From으로 시작되지 않으면 무시해라
    if len(bro) < 3 or bro[0] != "From" :
        continue
    print(bro[2])
