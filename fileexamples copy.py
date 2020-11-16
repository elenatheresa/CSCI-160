'''
fileName = open('week.txt','w') #open('name of the file','mode in which you are dealing with the file')
# 'w' will check to see if this file exists, and if it does then it will be created

fileName.write(str(1) + '\n')
fileName.write(str(2) + '\n')
fileName.write(str(3) + '\n')
fileName.write(str(4) + '\n')
fileName.write(str(5) + '\n')
fileName.write(str(6) + '\n')
fileName.write(str(7) + '\n')

fileName.close()
'''
'''
fileName1 = open('week.txt','r')
fileName1.read() 
print(fileName1.read()) #reading all lines of a file as a string 
print(fileName1.readline()) #read lines one at a time 
print(fileName1.readlines()) # read all the data and will give data as a list 
fileName1.close() #always close

#writelines - allows user to give the input in the form of list
'''

'''
default mode is 'r', and default file mode is 'txt'
'''

'''
fileName2 = open('week.txt','a') 
fileName2.write(str(8) + '\n') # only adding at the end
fileName2.close()
'''

import os
fileName = input("ender a file name: ")
if os.path.exists(fileName):
    with open(fileName,'a') as fileName3: # this allows you to not have to use the .close command
        fileName.write(str(9) + '\n')
else:
    print("there is no such file")
