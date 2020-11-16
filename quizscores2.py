'''
Initialize event-controlled loop

Accepts quiz scores until the user enters an invalid quiz score - -1 for
this program

'''
highScore = -1
lowScore = 1000
totalPoints = 0

numOfStudents = 0 #initialize counter to 0 BEFORE the loop
quizScore = int ( input ("Enter the first quiz score (0-10). Enter -1 to quit."))
#while quizScore != -1:
while quizScore >= 0 and quizScore <= 10:
   #reason for the loop
   numOfStudents = numOfStudents + 1 #increment our counter
   totalPoints = totalPoints + quizScore
   
   if quizScore > highScore:
      highScore = quizScore
   if quizScore < lowScore:
      lowScore = quizScore
      
   quizScore = int ( input ("Enter the next quiz score "))



# and now find the average and print out all the other information
if numOfStudents != 0:
   average = totalPoints / numOfStudents
   print ("The class averare is ", format (average, "1.2f" ))
#else:
#   print ("user entered 0 students, nothing to do")


if numOfStudents != 0:
   average = totalPoints / numOfStudents
else:
   average = 0
print ("Number of students taking the quiz ", format (numOfStudents, "5d"))   
print ("The class averare is               ", format (average, "5.2f" ))
print ("The highest score is               ", format (highScore, "5d"))
print ("the lowest score is                ", format (lowScore, "5d"))
