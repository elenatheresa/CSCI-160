percentage = float ( input ("Enter your class percentage "))

grade = "Z"

if percentage >= 90:
   grade = "A"
elif percentage >= 70:
   grade = "C"
elif percentage >= 80:
   grade = "B"
elif percentage >= 60:
   grade = "D"
else: # or elif percentage < 60:
   grade = "F"

print ("Your grade is ", grade )
                     
