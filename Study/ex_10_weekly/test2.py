lst = ['10-a','10-b','1-1','7-2']
tmp = []
for wd in lst :
    tup = wd.split('-')
    tmp.append( (int(tup[0]),tup[1])  )

for tup in sorted(tmp) :
    print(str(tup[0]) + '-' + tup[1])
