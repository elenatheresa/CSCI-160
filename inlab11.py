'''
elena corpus
csci 160
tuesday 5 - 7
ask how many integer values will be stored in the list
'''

import math

def theSum(theList):
    totalSum = 0
    for num in theList:
        totalSum = totalSum + num
    return totalSum

def theAverage(theList):
    sumOfList = theSum(theList)
    count = 0
    for num in theList:
        count = count + 1
    if count == 0:
        return 'Average cannot be calculated'
    return sumOfList / count 

def inOrder(theList):
    for num in range(0, len(theList) - 1):
        if theList[num] > theList[num + 1]:
            return False
    return True

def theMedian(theList):
    theList.sort()
    if len(theList) % 2 != 0:
        median = theList[(0 + (len(theList) - 1)) // 2]
    else:
        median = (theList[math.floor((0 + (len(theList) - 1)) / 2)] + theList[math.ceil((0 + (len(theList) - 1)) / 2)]) / 2
    return median

def printValues(theList):
    print('index  Value')
    for num in range(0, len(theList)):
        print(format(num,'<6d'), format(theList[num], '6d'))

numInList = int(input('how many integers are in this list? '))

numList = [ ]

for num in range(0, numInList):
    userNum = int(input('enter a value: '))
    if 1 <= userNum <= 9999:
        numList.append(userNum)
    
print('the sum of numbers in the list: ',theSum(numList))

print('the average of numbers in a list: ', theAverage(numList))

print('is list in order? ', inOrder(numList))

print('the median number of a list: ', theMedian(numList))

printValues(numList)

