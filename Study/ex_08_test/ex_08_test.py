han = open("romeo.txt")

sumlist = []

for line in han:
    line = line.rstrip()
    list_of_words = line.split(" ")
    sumlist = sumlist + list_of_words
print(sumlist)

while True:
    newword = input("새 단어를 입력하세요=>")
    if newword == "done" :
        break
    elif newword not in sumlist :
        print("New word!")
        sumlist.append(newword)

list.sort(sumlist)
print(sumlist)
