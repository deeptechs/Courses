# Worked Exercise 5.1

largest = None
smallest = None
sum = 0
count = 0
while True:
    
    try:
        num = raw_input("Enter a number: ")
        if num == "done" : 
            break
        else:
            num = int(num)
            count = count + 1
            sum = sum + num
            if largest is None:
                largest = num
            else:
                if largest < num:
                   largest = num
            if smallest is None:
                smallest = num
            else:
                if smallest > num:
                   smallest = num
    
    except:
        print 'Invalid input'

print "Maximum is", largest
print "Minimum is", smallest
print "Sum is", sum
print "Counter is", count
print "Average is", float(sum) / count
