'''
elena corpus
csci 160
tuesday 5 -7 pm
program to ask for data file, and then finding data from it
'''

fileName = open('testscores.txt','r')

def largestScore():
    fileName.readlines()
    num = int(fileName)
    for num in range(0,101):
        if num <= 99:
            num = largestScore
        elif num <= 80: 
            num = largestScore
        elif num <= 60: 
            num = largestScore
        elif num <= 40: 
            num = largestScore
        else:
            num = largestScore

def smallestScore():
    fileName.readlines()
    num = int(fileName)
    for num in range(0,101):
        if num < 10:
            num = smallestScore
        elif num <= 40: 
           num = smallestScore
        elif num <= 60: 
           num = smallestScore
        elif num <= 80: 
           num = smallestScore
        else:
            num = smallestScore
            
totalNum = 0

fileName.readlines()
for lines in fileName:
    totalNum = totalNum + 1
    num = num + num 

print('Searching for values')
upperLimit = input('Enter the upper limit: ')
lowerLimit = input('Enter the lower limit: ')

if num > lowerLimit and num < upperLimit:
    print(num)

print('Largest Score:', largestScore)
print('Smallest Score:', smallestScore)
print('Average scores:', averageScore)



fileName.close()
