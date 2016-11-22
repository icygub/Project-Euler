def sumSquares():
    sumSquares = 0
    for number in range(1,101):
        sumSquares = sumSquares + (number * number)

    return sumSquares

def squareSum():
    theSum = 0
    for number in range(1,101):
        theSum = theSum + number
    squareSum = theSum * theSum    
    return squareSum


def main():
    diff = squareSum() - sumSquares()
    print(diff)


    

if __name__ == '__main__':
    main()
