'''
elena corpus
csci 160 5:00-7:00
inlab 3 
'''

num = float(input("Enter a numeric value: "))

#finding the whole number 
if num.is_integer():
    if int(num) >= 0:
        print("given number is a whole number")
    else:
        print("given number is not a whole number")
else:
    print("given number is not a whole number")

# finding whether a number is multiple of 5 or not 
if num % 5 == 0:
    print("given number is a multiple of five")
else:
    print("given number is not a multiple of five")
    
#finding if the value is even or odd
if num % 2:
    print("given number is even")
else:
    print("given number is odd")

#finding if a value is positive, negative or zero
if num > 0:
    print("given number is positive")
elif num == 0 :
    print ("given number is zero")
elif num < 0:
    print ("given numbe is negative")

#finding if a value is within the range of 2010 to 2018
if num >= 2010 and num <= 2018:
    print ("given number is within the range")
else:
    print("given number is not within the range")

#finding if value is three digits, starting with 1
if num >= 100 and num <= 199: 
    print("given number is in 100s")
else:
    print("given number is not in 100s")

#second value from user
#part 2
num2 = (float(input("enter a second number: "))

#getting the largest of two numbers
if num == num2:
    print("first number is greater than second:", num)
elif num2 > num:
    print("second number is greater than the first: ", num2)
else :
    print("they are equal")

#second value is or not a multiple of the first value
if num2 % num == 0:
    print("second value is a multiple of the first value")
else:
    print("second value is not a multiple of the first value")

#first value is or not a mulitple of the second value
if num % num2 == 0:
    print("first value is a multiple of the second value")
else:
    print("first value is not a multiple of the second value")
