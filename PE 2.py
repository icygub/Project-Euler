#Project 2
#Even Fibonacci numbers
#By: Icygub 10/16/2016
#Description: Totals fibonacci sequence of even values. Stops adding when fibonacci number is greater than 4000000

def printFibonacci():
    totalFib = 0
    sumOfEven = 0
    prevFib = 0
    currentFib = 1
    
    while (totalFib < 4000000):
        totalFib = currentFib + prevFib
        if (totalFib % 2 == 0):
            sumOfEven += totalFib
        prevFib = currentFib
        currentFib = totalFib
    print (str(sumOfEven))    
printFibonacci()

