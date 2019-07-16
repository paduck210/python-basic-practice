d = dict()
d["csev"] = 2
d["cwen"] = 4
for (k, v) in d.items():
    print(k,v)

#딕셔너리에 뭐가 있는지 궁금하다면
#딕셔너리에 내장된 items()메소드 사용가능
tups = d.items()
print(tups)
