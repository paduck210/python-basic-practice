kr_women = {220: 5, 225: 5.5, 230: 6}

us_women = list()
for k, v in kr_women.items() :
    us_women.append((v, k))
us_women = dict(us_women)
# NOTE: us_women = {5: 220, 5.5: 225, 6: 230}

ask = float(input('Enter Your shose size: '))

if ask > 219:
    # Korea
    print("KR SIZE=", ask)
    print("US SIZE=", kr_women.get(int(ask)))
elif ask < 11:
    # USA
    print("US SIZE=", ask)
    print("KR SIZE=", us_women.get(ask))
else:
    print("유효하지 않습니다")

if ask > 219:
    # Korea
    print("KR_SIZE=", ask)
    print("US_SIZE=", float((ask - 220) * 0.1 + 5))
elif ask < 11:
    # USA
    print("US SIZE=", ask)
    print("KR SIZE=", int((ask - 5) * 10 + 220))
else:
    print("유효하지 않습니다")
