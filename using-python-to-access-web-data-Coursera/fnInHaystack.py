import re

fName = input("Insert File Name:")

if len(fName) < 1:
    fName = "regex_sum_11842.txt"

fHandle = open(fName)

lst = list()
for line in fHandle:
    nums = re.findall('[0-9]+', line)
    lst.extend(nums)

total = 0
for i in lst:
    total = total + int(i)

print(total)

# One Line Solution
print( sum( [ int(s) for s in re.findall('[0-9]+',open('regex_sum_11842.txt').read()) ] ) )
