startValue = int ( input ("Enter the starting value "))
endValue = int ( input ("Enter the ending value "))
#stepValue = int ( input ("Enter the step "))

if startValue < endValue:
   for value in range (startValue, endValue + 1, 1):
      print (value)
else:
   for value in range (startValue, endValue - 1, -1):
      print (value)
