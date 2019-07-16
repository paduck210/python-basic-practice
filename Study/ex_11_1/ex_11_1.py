hand = open("mbox-short.txt")
for line in hand:
    line = line.rstrip()
    if line.startswith('From:') :
        print(line)

print("="*60)
#######################################################

import re

hand2 = open("mbox-short.txt")
for line2 in hand2 :
    line2 = line2.rstrip()
    if re.search('^From:', line2) :
        print(line2)


print("="*60)
#######################################################

for line3 in hand2 :
    line3 = line3.rstrip()
    if re.search(" ^X.*: ", line3) :
        print(line3)
