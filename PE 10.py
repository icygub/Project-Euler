#Project Euler 10
#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.
#ANSWER: 

def calcSum():
    NUMBER = 2000000 #2 is prime, but will not be calculated, so primeNum = 3
    sumPrimes = 17 #2+3+5+7 = 17
    num = 11
    isPrime = True
    while (num < NUMBER):
        for div in range(3, int(num/2), 2):        
            if (num % div == 0): #if even only once, then its not prime
                isPrime = False
                break
           
        if (isPrime): #if there was no even divisor in for loop
            sumPrimes = sumPrimes + num
        num = num + 2     
        isPrime = True
    return sumPrimes
        

def main():
    print('Sum of primes below two million: ' + str(calcSum()))

if __name__ == '__main__':
    main()
