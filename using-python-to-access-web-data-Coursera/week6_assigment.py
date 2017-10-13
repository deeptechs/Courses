import urllib.request

import json

html = urllib.request.urlopen("http://py4e-data.dr-chuck.net/comments_11847.json")

tree = html.read().decode()

js = json.loads(tree)

sum = 0
for person in js["comments"]:
    sum = sum + int(person["count"])

print(sum)
