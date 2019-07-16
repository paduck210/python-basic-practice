typing = input("파일명을 입력하세요: ")
fhand = open(typing)

counts = dict()
for line in fhand :
    words = line.split()
    for word in words :
        counts[word] = counts.get(word,0) + 1

####edit
