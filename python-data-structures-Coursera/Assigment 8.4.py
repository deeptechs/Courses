fname = input("Enter file name: ")
fh = open(fname)

lst = list()

for line in fh:
    temp = line.split()
    for tm in temp:
       if tm not in lst:
        lst.append(tm)

print(sorted(lst))