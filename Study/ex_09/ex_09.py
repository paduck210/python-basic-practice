fname = input("Enter file name: ")
if len(fname) < 1 : fname = "clown.txt"
hand = open(fname)

di = dict()
for line in hand :
    line = line.rstrip()
    words = line.split()
    for w in words :
        #idiom : retieve / create / upddate counter
        di[w] = di.get(w,0) + 1
#print(di)


#now we want to find the most common words


largest = -1
theword = None
for kkk, vvv in di.items() :
    if vvv > largest :
        largest = vvv
        theword = kkk #capturre/remember the word that was largest

print ("Done", theword, largest)
