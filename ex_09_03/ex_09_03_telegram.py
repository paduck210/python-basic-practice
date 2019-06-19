name = input("파일명을 입력하시오: ")
handle = open(name)


#빈 딕셔너리를 만들고
counts = dict()

#위>아래로 한줄씩 읽으면서
#왼>오른 순으로 단어별로 자르고
#단어의 히스토그램을 만들어낸다
for line in handle :

    if "<" in line or ">" in line :
        continue
    line = line.rstrip()
    words = line.split()
    for word in words :
        counts[word] = counts.get(word,0) + 1



#제일 빈도수가 많이 나온 단어를 찾는 방식
bigword = None
bignumber = None
for word,count in counts.items() :
    if bignumber is None or count > bignumber :
        bigword = word
        bignumber = count

print(bigword,bignumber)
