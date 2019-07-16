lst = ['10-a','10-b','1-1','7-2']
tmp = []
for wd in lst :
    tup = wd.split('-')
    tmp.append(tup[0],tup[1])
print(tmp)
