import os
import FileUtils

#fileName = "datafile.txt" #input ("Enter file name ")
fileName = FileUtils.selectOpenFile ("Select data file to open", "Read File Example")

if fileName == None: #user pressed cancel/X
   os._exit(0)
   
#check if the file actually exists before trying to open the file
if os.path.isfile (fileName) == False:
   print ("Data file does not exist")
   os._exit(0) #ends the program

inFile = open (fileName, "r") #we will read, or receive info from the data file

numOfStudents = 0
total = 0
for line in inFile:
   line = line.rstrip() #remove the linefeed that is part of any data returned from the file
   numOfStudents = numOfStudents + 1
   total = total + int(line)
   
   print (line)

inFile.close()

if numOfStudents != 0:
   average = total / numOfStudents
   print ("Total of the values:  ", total)
   print ("Averge of the values: ", format (average, "1.2f"))
else:
   print ("Nothing there")
