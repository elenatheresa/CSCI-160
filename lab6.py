'''
Elena Corpus
CSCI 160
Tuesday 5 - 7 pm
writing functions
'''
import math

def inputWithinRange (lowValue,highValue):
'''
num inputed must be within the range of 0 and 100.
will return true is the number inputed is within this range, false if it isnt
'''
    num = int(input("Enter a number: "))
    lowValue = 0
    highValue = 100
    if num > lowValue and num < highValue:
        return true 
    else :
        return false 

def doContinue (prompt) :
'''
asks user to enter yes or no
will be true is it is a yes, false if enters no
'''
    x = input("Enter yes or no: ")
    if x.upper() == "yes" or x.lower() == "yes":
        return true
    elif x.lower() == "no" or x.lower() == "no":
        return false 

def square (intValue):
'''
User enters the value and it returns the squared number
'''
    intValue = input("Enter a number: ")
    return intValue**2 

def summation (intValue):
'''
user enters a number and the function will return the summation
of the number inputed
'''
    intValue = input("Enter a value: ")
    return intValue * (intValue + 1) // 2 

def sumOfSquare (intValue):
'''
user enters a number and the function returns the sum of the squares of
the number entered
returning either zero if zero was entered or the sum of the squares
if the value is larger than zero
'''
    intValue = input("Enter a value: ")
    if intValue == 0:
        return 0
    else:
        return sumOfSquare(intValue - 1) + sumSquares (n - 1) 
    

def factorial (intValue):
'''
user enters intValue and factors the number and adds all the numbers
together, and returning the sum
'''
    intValue = input("Enter value: ")
    y = 1
    while intValue > 0:
        y = y * intValue
        x -= 1
    return y 

def distance (x1,y1,x2,y2):
'''
user enters two sets of points, and use those numbers to find 
the distance between the points and return the distance
'''d
    x1 = input("Enter the first x value: ")
    x2 = input("Enter the second x value: ")
    y1 = input("Enter the first y value: ")
    y2 = input("Enter the second y value: ")
    sq1 = (x1-x2)*(x1-x2)
    sq2 = (y1-y1)*(y1-y2)
    return math.sqrt(sq1 + sq2)

def isOdd (intvalue):
'''
user enters a value and the function returns if it is an odd number
or not
'''
    intValue = input("Enter a number: ")
    if invalue % 1: 
        return true 
    else :
        return false 

def isEven (intValue):
'''
user enters a value and the function returns if it is an even number
or not
'''
    intValue = input("Enter a number: ")
    if intValue // 2:
        return true  
    else :
        return false


