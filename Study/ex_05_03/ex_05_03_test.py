#IQ 정의

paduck = 40
sadary = 50
max = 80
gimo = 150
joon = 160
rina = 190

largestIQ = 0

#print ('누구의 IQ가 제일 높을까?=')
#for IQ in [paduck, sadary, max, gimo, joon, rina] :
#    if IQ >= largestIQ:
#        print(IQ)
#        largestIQ = IQ
#print ("Finish = ", largestIQ)

#print ("=" * 30)

dict = {'paduck': 40, 'sadary': 160, 'max': 80, 'gimo': 150, 'joon': 90, 'rina': 100}

paduck = 40
dict['paduck'] = 40
print(sadary)

#print("Dictionary=", dict)
#print("Items=", dict.items())

largestIQ = 0
largestname = "nobody"
for name, IQ in dict.items():
    if IQ >= largestIQ:
        print("중간 1등", name, IQ)
        largestIQ = IQ
        largestname = name
print ("Finish=", largestname, largestIQ)
