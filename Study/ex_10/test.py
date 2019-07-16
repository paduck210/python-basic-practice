fhand = open ('mbox-short.txt')
counts = dict()

for line in fhand :
    line = line.rstrip()
    if not line.startswith("From") :
        continue
    word = line.split()
#    word[1] 이 메일주소인데... 이게 왜
    print(word)
#    print(word[1:2])
#    print(word[1])
