import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

count = 7
position = 18
in_position = 0

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/known_by_Anjolaoluwa.html"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
for i in range(count):
    tags = soup('a')
    for tag in tags:
        url = tag.get('href', None)
        if url is not None:
            in_position = in_position + 1;
            if in_position == 18:
                html = urllib.request.urlopen(url, context=ctx).read()
                soup = BeautifulSoup(html, 'html.parser')
                in_position = 0
                break
    name = tag.text
print(name)