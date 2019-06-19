fname = input ("Enter filie name: ")
if len(fname) < 1 :
    fname = 'mbox-short.txt'
fhand = open(fname)

#빈 딕셔너리에 넣기
counts = dict()
for line in fhand :
    line = line.rstrip()
    if not line.startswith("From") :
        continue
    word = line.split()

#중요! 딕셔너리화가 되는 카운트 단위는 리스트여야 함
#word[2]로 카운트하면 [] 리스트가 아닌 "str"이 되버림
    mlist = word[1:2]
    for mail in mlist :
        counts[mail] = counts.get(mail,0) + 1

#딕셔너리 > 튜플단위로 리스트화
lst = list()
for (k,v) in counts.items() :
    newup = (v,k)
    lst.append(newup)
    #print(newup)

#튜플 정렬
lst = sorted(lst,reverse=True)
for (v,k) in lst[:1] :
    print(k,v)
