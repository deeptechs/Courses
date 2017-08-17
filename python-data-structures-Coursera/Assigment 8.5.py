fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
lst = list()

try:
 for line in fh:
    abc = line.rstrip()
    if not abc.startswith('From ') : 
       continue
    abc = line.split()
    lst.append(abc[1])
    # Guardian for the error
    if len(abc) > 1:
     print(abc[1])
except:
    print("error")
    print(len(abc))
    
print("There were", len(lst), "lines in the file with From as the first word")