import urllib.request
import xml.etree.ElementTree as xm

html = urllib.request.urlopen("http://py4e-data.dr-chuck.net/comments_11846.xml")

tree = xm.fromstring(html.read().decode())

sum = 0
for child in tree:
    for inchild in child:
        if inchild.tag == "comment":
            sum = sum + int(inchild.find('count').text)

print(sum)
