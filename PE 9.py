#Project Euler 9
#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a*a + b*b = c*c
#For example, 32 + 42 = 9 + 16 = 25 = 52.
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.
#ANSWER: 31875000

def findAnswer():
    c = 0.0

    for a in range(1, 500):
        for b in range(a+1,500):
            c = (a**2 + b**2)**.5
            if(a + b + c == 1000):
                return a*b*c

def main():
    print('Product of abc, where a + b + c = 1000, is: ' + str(findAnswer()))
            
if __name__ == '__main__':
    main()
