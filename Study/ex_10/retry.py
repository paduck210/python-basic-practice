#파일열기
fname = input ("텍스트값을 입력하시오: ")
if len(fname) < 1 :
    fname = 'mbox-short.txt'
fhand = open(fname)

#딕셔너리 만들기
count = {}
for line in fhand :
    line.rstrip()
    if not line.startswith("From") :
        continue
    words = line.split()
    mails = words[1:2]
    for mail in mails :
        count[mail] = count.get(mail,0) + 1

#딕셔너리 - 튜플 단위 리스트화
lst = []
for (k,v) in count.items() :
    newup = (v,k)
    lst.append(newup)

#튜플 정렬
lst = sorted(lst, reverse=True)
for (v,k) in lst[0:5] :
    print(k,v)
