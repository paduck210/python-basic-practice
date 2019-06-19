import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://onepound.kr/')

for line in fhand:
    print(line.decode().strip())
