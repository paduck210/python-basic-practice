#파일열고 딕셔너리 화
fhand = open("romeo.txt")
counts = dict()
for line in fhand :
    words = line.split()
    for word in words :
        counts[word] = counts.get(word,0) + 1


#튜플 + 리스트화
lst = list()
for k,v in counts.items() :
    newup = (v,k)
    lst.append(newup)


#코드 줄이기
print(sorted([(v,k) for k,v in counts.items()]))
#print
#sorted ([   (v,k) (v,k) (v,k) (v,k)   ])






#value 기준 내림차 정렬
#lst = sorted(lst, reverse=True)
#for v, k in lst[:10] :
#    print(k,v)
