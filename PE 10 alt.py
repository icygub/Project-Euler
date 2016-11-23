#Project Euler 10
#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.
#ANSWER: 142913828922

def sum_of_primes_below(upper):
    prime_bools = sieve_of_eratosthenes(upper)
    sum_primes = 0
    for n in range(len(prime_bools)):
        if prime_bools[n]:
            sum_primes += n
    return sum_primes

def sieve_of_eratosthenes(upper):
    prime_bools = [True] * upper
    prime_bools[0] = False
    prime_bools[1] = False
    for i in range(2, upper):
        if prime_bools[i]:
            for x in range(i*i,upper, i):
                prime_bools[x] = False
    return prime_bools

def main():
    upper = int(input('This program will calculate sum of all primes below a number.\n Enter a number:'))
    print(sum_of_primes_below(upper))

if __name__ == '__main__':
    main()
