'''
elena corpus
csci 160
tuesday 5 - 7
read file and collect data on how many of each letter there is

fileName = open('lab11txtfile.txt')

letterFrequency = {}

def printSortedLetters(fileName, letterFrequency):
    sortedLetters = list(letterFrequency.keys())
    sortedletters.sort()
    for letters in letter:
        print(format(letters,'7s'),format(letterFrequency[letter],'>6d'))

#print(letterFrequency)

printSortedLetters(fileName)
  
fileName.close()
'''

def printSortedLetters(fileName, letterFreq):
    for numOfPasses in range(0,len(letterFreq) - 1):
        for index in range(o, len(letterFreq) - 1):
            if letterFreq[letter].lower > letterFreq[letter + 1].lower():
                num = letterFreq[index]
                letterFreq[index] = letterFreq[index + 1]
                letterFreq[index + 1] = num
                

fileName = open('lab11txtfile.txt')
letterFreq = {}
for word in fileName:
    for letter in word:
        keys = letterFreq.keys()
        if letter in keys:
            letterFreq[letter] += 1
        else:
            letterFreq[letter] = 1

print(letterFreq)
printSortedLetters(fileName)
