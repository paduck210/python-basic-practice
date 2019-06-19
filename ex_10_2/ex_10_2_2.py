d = {'a':10, 'b':4, 'e':22, 'd':11, 'c':5}
tmp = list()

#빈 리스트에 / 위 딕셔너리의 튜플값을 원소를 넣어라
for k,v in d.items() :
    tmp.append( (v,k) )

tmp = sorted(tmp, reverse=True)
print(tmp)
#결과값 = [(22, 'e'), (11, 'd'), (10, 'a'), (5, 'c'), (4, 'b')]

for a,b in tmp :
    print(a,b)

#결과값
#22 e
#11 d
#10 a
#5 c
#4 b
