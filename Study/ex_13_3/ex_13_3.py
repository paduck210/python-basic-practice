import xml.etree.ElementTree as ET
tree = ET.parse('http://python-data.dr-chuck.net/comments_42.xml')
root = tree.getroot()

for country in root.iter("country") :
    print "=" *60

    print "Year :", country.findtext("year")
