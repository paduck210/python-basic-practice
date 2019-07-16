

emptylist = []

while True :
    inp = input("입력하세요")
    args = inp.split()

    if args[0] == 'done' :
        break
    elif args[0] == 'print' :
        print(emptylist)
    elif args[0] == 'append' :
        emptylist.append(args[1])

    elif args[0] == 'appends' :
        addlist = args[1].split(",")
        emptylist = emptylist + addlist

    elif args[0] == "in" :
        a = args[1] in emptylist
        print(a)

    elif args[0] == "notin" :
        b = args[1] not in emptylist
        print(b)

    elif args[0] == "remove" :
        emptylist.remove(args[1])

    else :
        print("worng")
