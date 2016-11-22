#Problem 1
#Multiple of 3 and 5
#By icygub
#Description: Find the sum of all multiples of 3 or 5 below a number

limit = 1000
sum = 0
for count in range(1,limit):
    if (count % 3 == 0):
        sum += count
    elif (count % 5 == 0):
        sum += count

print (str(sum))        
