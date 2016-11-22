#Project Euler 7
#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?
#11/18/2016
#icygub

#ANSWER: 104743

def calcPrime(location):
    num = 11 #2 is prime, but will not be calculated, so primeNum = 3
    primeCount = 5 #same reason as above
    isPrime = True
    while (True):
        for div in range(3, int(num/2), 2):        
            if (num % div == 0): #if even only once, then its not prime
                isPrime = False
                break
           
        if (isPrime): #if there was no even divisor in for loop
            if (primeCount == location):
                return num
            primeCount = primeCount + 1
    
        num = num + 2     
        isPrime = True
        

def main():
    print('Which prime would you like?\n' +
          'e.g. the 100th prime or the 8392th prime.\n' +
          'Enter an int greater or equal to 11')
    location = 0
    while (True):
        try:
            location = int(input())
            if(location >= 11):
                break
            else:
                print('Too small\n')
        except:
            print('Invalid input. Try again.\n')
    print('Prime number ' + str(location) + ' is: ' + str(calcPrime(location)))

if __name__ == '__main__':
    main()
