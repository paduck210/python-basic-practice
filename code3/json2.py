import json

data = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Brent"
  }
]'''

info = json.loads(data)
print("리스트 반환", info)
print('User count:', len(info))

#위 Data에서 보면 딕셔너리가 두개이므로, 딕셔너리를 차례대로 반복하는 의미
for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])
