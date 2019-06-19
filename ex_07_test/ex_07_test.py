#fh = open ("mbox-short.txt")
#print(fh)


#파일열기
#xfile = open("mbox-short.txt")
#for cheese in xfile :
#    cheese = cheese.rstrip()
#    print(cheese)


#텍스트파일이 몇줄인가
xfile = open("mbox-short.txt")
count = 0
for cheese in xfile :
    cheese = cheese.rstrip()
    count = count + 1
print ('Lince count:', count)


#문자수가 몇개인가
xfile = open("mbox-short.txt")
good = xfile.read()
print(len(good))


#특정값 찾기
xfile = open("mbox-short.txt")
for line in xfile :
    line = line.rstrip()
    if line.startswith('X-') :
        print(line)
