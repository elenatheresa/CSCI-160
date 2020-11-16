percentage = float ( input ("Enter your class percentage "))

grade = "Z"

if percentage >= 70:
   passedClass = True
   if percentage >= 90:
      grade = "A"
   elif percentage >= 80:
      grade = "B"
   else:
      grade = "C"
else:
   if percentage >= 60:
      grade = "D"
   else: # or elif percentage < 60:
      grade = "F"
   passedClass = False
   

print ("Your grade is ", grade )
#if passedClass == True:
#or
if passedClass: # or if not passedClass == False  
   print ("You passed the class using pass/fail" )                   
else:
   print ("You failed the class using pass/fail" )                   
