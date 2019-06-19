import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://onepound.kr/')

counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1


print(counts)

#bigword = None
#bignumber = None
#for word,count in counts.items() :
#    if word.startswith("<") :
#        continue
#    elif bignumber is None or count > bignumber :
#        bigword = word
#        bignumber = count

#print(bigword,bignumber)
