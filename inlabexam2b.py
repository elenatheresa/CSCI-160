'''
elena corpus
csci 160
tuesday 5 -7 pm
storing golf scores
'''

fileName = open('golfscores.txt','r')

if fileName == None:
    print('there is no such file')
    
theList = []

def numberOfStrokes(theList):
    totalScore = 0
    score = int(theList)
    while score in theList:
        totalScore = totalScore + score 
        if totalScore == 36:
            print('scored par')
        elif totalScore < 36:
            print('scored below par')
        else:
            print('scored above par')

def hadHoleInOne(theList):
    score = int(theList)
    foundOne = False
    while score in theList:
        if score == 1:
            foundOne = True
            print('congratulations on your hole-in-one!')
    foundOne = False

def printResults(theList):
    score = int(theList)
    print(format('hole', '6s'), format('score', '6s'))
    while score in theList:
        print(format('1' + index[0], '%d'))
        print(format('2' + index[1], '%d'))
        print(format('3' + index[2], '%d'))
        print(format('4' + index[3], '%d'))
        print(format('5' + index[4], '%d'))
        print(format('6' + index[5], '%d'))
        print(format('7' + index[6], '%d'))
        print(format('8' + index[7], '%d'))
        print(format('9' + index[-1],'%d'))


printResults()

print('total for the round:', numberOfStrokes)
numberOfStrokes()

hadHoleInOne()

    



