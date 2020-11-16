'''
elena corpus
ID: 1183721
Tuesday 5-7 pm
asking for file name and reading for all the values in the file
'''

import os
import FileUtils

fileName = 'hello.py'

if fileName == None:
    print("This file name does not exist")

inFile = open(fileName, 'r')

num = 0 
totalNum = 0

if num != 0:
    aveValue = totalNum / num
    print("the average: ",format(aveValue,".3f"))
    print("the total number of values: ",totalNum)
    print("The minimum value: ", min(num))
    print("The maximum value: ", max(num))

if int(num) >= 70:
    print("the total number of values greater than or equal to 70: ", num)
else:
    print("no data in file")

if int(num) > 70 or int(num) < 70: 
    print("the value closets to 70:
else:
    print("no data in file")

if int(num) < 70: 
    print("the value closet to 70 WITHOUT going over 70: "
else :
    print("no data in file")
