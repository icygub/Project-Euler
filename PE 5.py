starting = 2520
counter = starting
list = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

while(True):
    listTester = True
    for listCount in range(len(list)):
        if (not(counter % list[listCount] == 0)):
            listTester = False
            break
    if (listTester):
        print(str(counter) + ' yeahhhh')
        break
    counter = counter + 2

#answer: 232792560. This takes a long time to calculate
    
