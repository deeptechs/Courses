from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_11844.html"
html = urlopen(url, context=ctx).read()

# html parse
soup = BeautifulSoup(html, "html.parser")

sum = 0

# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    #print('TAG:', tag)
    #print('Contents:', tag.contents[0])
    if tag.attrs['class'][0] == "comments":
        sum = sum + int(tag.contents[0])

print(sum)