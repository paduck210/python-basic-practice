word = 'brrontosaurus'
d = dict()
for c in word :
    d[c] = d.get(c,0) + 1


print( sorted( [ (v,k) for k,v in d.items()   ] , reverse = True  )  )
