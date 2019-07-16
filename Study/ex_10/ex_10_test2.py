#v파일열기

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

#시간만 표기된 line거르기
    word = line.split()
    if not len(word) > 3 :
        continue

#시:분:초를 str으로 뽑고 > 위치값으로 시간만을 걸러서 > 리스트화
    fulltimes = word[5]
    hours = fulltimes[0:2]
    hourlst = list()
    hourlst.append(hours)

#딕셔너리 카운팅
    for hour in hourlst :
        counts[hour] = counts.get(hour,0) + 1

#딕셔너리 > 튜플단위로 리스트화
lst = list()
for (k,v) in counts.items() :
    newup = (k,v)
    lst.append(newup)

#튜읖정렬 - 오름차순으로
lst = sorted(lst,reverse=False)
for (k,v) in lst :
    print(k,v)
