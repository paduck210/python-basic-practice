
word = "brontosaurus"
d = dict()
for c in word :
    d[c] = d.get(c,0) + 1
print(d)


lst = list(d.keys())
lst.sort()
print(lst)

for key in lst :
    print(key,d[key])



#for key in list :
#  print(key,value)
