
def findPldrm(starting, current):
    for count in range(starting)[::-1]:
        first = str(current)[0]
        last = str(current)[len(str(current))-1]
        if (first == last):
            if (str(current)[1] == str(current)[len(str(current))-2]):
                if (str(current)[2] == str(current)[len(str(current))-3]):
                    print(current)
        current -= 1                

def main():
    starting = 998001
    current = 998001
    findPldrm(starting, current)
 
    
       
 
    #Start at 998001
    #Count down
    #test if last digit == first digit
    #if equal, then it will start calculating each number   
    #if last != first, it will skip the quantity it needs to until it
        #arrives at the next number where first == last
    #then continue calculates
    #any palindrome found will go into another function
    #this function will find the factors
    #if number has only two three-digit factors, number gets stored in
        #largestPal variable
    #if number does not pass that test, code will resume
    #first value that gets set as largestPal will be answer,
        #and the program will terminate
   
if __name__ == "__main__":
    main()
