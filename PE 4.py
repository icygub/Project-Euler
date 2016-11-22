def main(): 
    starting = 998001
    
    for current in range(starting, 0, -1):
        if (str(current)[0] == str(current)[len(str(current))-1]):
            if (str(current)[1] == str(current)[len(str(current))-2]):
                if (str(current)[2] == str(current)[len(str(current))-3]):
                    print(current)
                    findFactors(current)
                    break
    #Start at 998001
    #Count down
    #test if last digit == first digit
    #if equal, then it will start calculating each number    
    #if last != first, it will skip the quantity it needs to until it
    #arrives at the next number where first == last
    #then continue calculates
    #any palindrome found will go into another function
                
def findFactors(current):
    if (current % 2 == 0):
        botRange = 2
    else:
        botRange = 3
        
    for divisor in range(botRange, current, 2):
        if (current % divisor == 0):
            print(str(divisor))
            break

    #if current is even, for loop will start at 2
    #if odd, for loop will start at 3
    #use for loop to find first number that divides evenly with current
    #save the divisor in an int, and the quotient in another int
    #call findFactors(quotient), which is recursive
    #
    print()
    
    
if __name__ == "__main__":
    main()
