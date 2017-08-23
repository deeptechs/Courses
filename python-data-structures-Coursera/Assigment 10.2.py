#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1: name = "mbox-short.txt"
handle = open(name)

hours = dict()
for line in handle:
    if line.startswith('From '):
        words = line.split(':')
        st = words[0]
        st = st.split()
        hour = st[len(st)-1]
        hours[hour] = hours.get(hour, 0) + 1

# Sort By Key
hours = sorted(hours.items())
for i, j in hours:
    print(i, j)

# Sort by Value
# lst = list()
# for i, j in hours.items():
#     newtup = j, i
#     lst.append(newtup)
#
# lst = sorted(lst)
# for i, j in lst:
#     print(i, j)

