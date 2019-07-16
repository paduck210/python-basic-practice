counts = dict()

xfile = open("kakaotalk.csv")

for lines in xfile :
    lines = lines.rstrip()
    words = lines.split()

print("단어결과",words)


#print("계산중...")

#for word in words :
#    counts[word] = counts.get(word,1) + 1

#print("계산결과", counts)
