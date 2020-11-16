'''
elena corpus
csci 160
tuesday 160
Part 2 : creating a datafile that contains a series of integer values,
per line
'''

fileName = open('numbers.txt','w') #open('name of the file','mode in which you are dealing with the file')
# 'w' will check to see if this file exists, and if it does then it will be created

fileName.write(str(100) + '\n')
fileName.write(str(-22) + '\n')
fileName.write(str(-3) + '\n')
fileName.write(str(40) + '\n')
fileName.write(str(55) + '\n')
fileName.write(str(63) + '\n')
fileName.write(str(-7) + '\n')

fileName.close()

