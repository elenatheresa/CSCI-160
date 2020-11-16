percentage = float ( input ("Enter your class percentage "))

grade = "Z"

if percentage >= 90:
   grade = "A"

if percentage >= 80 and percentage < 90:
   grade = "B"

if percentage >= 70 and percentage < 80:
   grade = "C"

if percentage >= 60 and percentage < 70:
   grade = "D"

if percentage < 60:
   grade = "F"

print ("Your grade is ", grade )
                     
