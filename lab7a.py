'''
elena corpus
ID: 1183721
Tuesday 5-7 pm
asking for file name nad then asking for test scores
'''
import os
import FileUtils

fileName = "hello.py"

if fileName == None:
    os._exit(0)

outFile = open(fileName, 'w')
testScores = input("Enter the test scores: ")

for testScores in range(0,101):
    outFile.write (str(testScores))
    
    
outFile.close()
