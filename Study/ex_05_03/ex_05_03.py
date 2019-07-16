#최저값을 임의로 잡아둔

largest = 1
print ('Start=',largest)
for num in [9,1029,2039,19288,29291,2828,1015,3342,1512] :
    if num > largest :
        largest = num
    print(largest,num)
print ("Finish=", largest)
