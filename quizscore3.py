numOfStudents = int ( input ("How many students took the quiz? "))

totalPoints = 0
highestScore = -1
lowestScore = 1000
MAX_SCORE = 10

for studentNum in range (1, numOfStudents + 1):
   #reason for the loop
   
   quizScore = int (input ("Enter quiz score for " + str(studentNum) + " "))
   while quizScore < 0 or quizScore > MAX_SCORE:
      print ("Please enter a valid quiz score between 0 and " + str(MAX_SCORE))
      quizScore = int (input ("Enter quiz score for " + str(studentNum) + " "))
      

   if quizScore > highestScore:
       highestScore = quizScore
   if quizScore < lowestScore:
       lowestScore = quizScore
   
   totalPoints = totalPoints + quizScore  #running total
   


if numOfStudents != 0:
   average = totalPoints / numOfStudents
   print ("The class averare is ", format (average, "1.2f" ))
#else:
#   print ("user entered 0 students, nothing to do")


print ()
if numOfStudents != 0:
   average = totalPoints / numOfStudents
else:
   average = 0
print ("The class average is ", format (average, "6.2f" ))
print ("The highest score is ", format (highestScore, "6d"))
print ("the lowest Score is  ", format (lowestScore, "6d"))
