import FileUtils
import os

#fileName = input ("Enter name of data file to create: ")
#fileName = 'datafile.txt'
fileName = FileUtils.selectSaveFile ("Select file for saving", "Write File Example")

if fileName == None: #user pressed cancel
   os._exit(0) #exit the program
   
#print ("Filename: ", fileName)
outFile = open (fileName, "w")
target = int (input ("How high should the program count? "))

for value in range (1, target + 1):
    outFile.write (str(value) + "\n") #must take a string value including it's delimiter

outFile.close()
