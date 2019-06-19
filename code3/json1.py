import json

#중괄호니까 딕셔너리

data = '''
{
  "name" : "Chuck",
  "phone" : {
    "type" : "intl",
    "number" : "+1 734 303 4456"
   },
   "email" : {
     "hide" : "yes"
   }
}'''

info = json.loads(data)

print('딕셔너리반환', info)
print('Name:', info["name"])
print('Hide:', info["email"]["hide"])
