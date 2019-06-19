counts = dict()

xfile = open("news.txt")

for lines in xfile :
    lines = lines.rstrip()
    words = lines.split()

print("단어결과",words)

print("계산중...")

for word in words :
    counts[word] = counts.get(word,1) + 1

print("계산결과")

#한줄씩 배열로 보여주기
for key in counts :
    print(key, counts[key])
