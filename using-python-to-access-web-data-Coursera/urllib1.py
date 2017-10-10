import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()
for line in fhand:
    for inline in line.decode().split():
        counts[inline] = counts.get(inline,0) + 1

print(counts)