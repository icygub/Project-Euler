#Project 3
#Largest prime factor
#By: Icygub 10/16/2016
#Description: Finds the largest prime factor of 600851475142
#600851475143

def findPrimeFactor(lowerRange, upperRange):    
    #this loop tests every odd number
    for count in range(lowerRange, upperRange, 2):
        #if current odd number divides with upperRange
        if (upperRange % count == 0):
            #result of that division is the largestFactor(may or may not be a prime)
            largestFactor = int(upperRange / count)
            print(str(largestFactor))
            findPrimeFactor((count + 2), largestFactor)
            break
    print (str(largestPrimeFactor))
lowRange = 3
upRange = 600851475143
compPrimeFactor = 0
largestFactor = 0
largestPrimeFactor = 0
findPrimeFactor(lowRange, upRange);
    
