'''
Initialize event-controlled loop

Accepts quiz scores until the user enters an invalid quiz score - -1 for
this program

'''

def intInput (prompt, lowLimit, highLimit):
   value = int ( input (prompt))
   while value < lowLimit  or value > highLimit:
      print ("Please enter a value integer value.\n")
      value = int ( input (prompt))

   return value
   
highScore = -1
lowScore = 1000
totalPoints = 0

age = intInput ("Enter your age", 0, 120)
year = intInput ("Enter year you were born ", 1900, 2018)
month = intInput ("Enter month you were born (1-12): ", 1, 12)
#if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
if month in [1, 3, 5, 7, 8, 10, 12]:
   day = intInput ("Enter day you were born (1-31): ", 1, 31)
elif month == 4 or month == 6 or month == 9 or month == 11:    
   day = intInput ("Enter day you were born (1-30): ", 1, 30)
elif year % 4 == 0: #leap year   
   day = intInput ("Enter day you were born ", 1, 29)
else:   
   day = intInput ("Enter day you were born ", 1, 28)

day = intInput ("Enter day you were born ", 1, dayInMonth)
print ("You are", age, "years old.")

numOfStudents = 0 #initialize counter to 0 BEFORE the loop
#quizScore = int ( input ("Enter the first quiz score (0-10). Enter -1 to quit."))
quizScore = intInput ("Enter the first quiz score (0-10). Enter -1 to quit.", -1, 10)
#while quizScore != -1:
while quizScore >= 0 and quizScore <= 10:
   #reason for the loop
   numOfStudents = numOfStudents + 1 #increment our counter
   totalPoints = totalPoints + quizScore
   
   if quizScore > highScore:
      highScore = quizScore
   if quizScore < lowScore:
      lowScore = quizScore
      
   quizScore = intInput ("Enter the next quiz score ", -1, 10)
   #quizScore = int ( input ("Enter the next quiz score "))



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
