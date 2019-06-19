#items 함수는 Key와 value값의 쌍을 튜플로 묶은 값을 dict_items 객체로 돌려준다
#items 함수로 딕셔너리 = (튜플),(튜플)들로 이루어진 [ 리스트화 ] 처리
d = {'a':10, 'b':4, 'e':22, 'd':11, 'c':5}
a = d.items()
print(a)
#결과값 = dict_items([('a', 10), ('b', 4), ('e', 22), ('d', 11), ('c', 5)])


#튜플 원소값 중 앞 key를 기준으로 정렬
b = sorted(d.items())
print("sorted정렬",b)
#결과값 = [('a', 10), ('b', 4), ('c', 5), ('d', 11), ('e', 22)]

#이걸 for 문으로 돌리면
for k,v in sorted(d.items()) :
    print(k,v)

#결과값
#a 10
#b 4
#c 5
#d 11
