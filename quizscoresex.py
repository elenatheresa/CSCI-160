numOfStudents = int ( input ("How many students took the quiz? "))

studentNum = 1
totalPoints = 0
highestScore = -1
lowestScore = 1000

while studentNum <= numOfStudents:
   #reason for the loop
   quizScore = int (input ("Enter quiz score for " + str(studentNum) + " "))

   if quizScore > highestScore:
       highestScore = quizScore
   if quizScore < lowestScore:
       lowestScore = quizScore
   
   totalPoints = totalPoints + quizScore  #running total
   

   studentNum = studentNum + 1 #counter

if numOfStudents != 0:
   average = totalPoints / numOfStudents
   print ("The class averare is ", format (average, "1.2f" ))
#else:
#   print ("user entered 0 students, nothing to do")


if numOfStudents != 0:
   average = totalPoints / numOfStudents
else:
   average = 0
print ("The class averare is ", format (average, "1.2f" ))
print ("The highest score is ", highestScore)
print ("the lowest Score is ", lowestScore)
