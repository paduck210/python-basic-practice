str = 'X-DSPAM-Confidence: 0.8475'

point = str.find("0")
print(point)
a = str[20:]
print(a)
# >> string

b = float(a)
print(b)
print(type(b))
