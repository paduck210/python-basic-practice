
count = 0
sum = 0

while True :

    quest = input ("ENTER A NUMBER:")

    if quest == "done" :
        
        break

    try :
        value = int(quest)
        sum = sum + value
        count = count + 1
        continue


    except :
        print ("Invalid number")
        continue

print (sum,count,sum/count)
