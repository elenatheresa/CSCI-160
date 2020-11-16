TIME_FRAME = 15   
for hour in range (9, 12 + 1):
   for minute in range (0, 60, TIME_FRAME):
      print (format (hour, "2d"), ":", format (minute, "02d"), sep='')

for hour in range (1, 4):
   for minute in range (0, 60, TIME_FRAME):
      print (format (hour, "2d"), format (minute, "02d"), sep=":")

hour = 4
minute = 0
print (format (hour, "2d"), format (minute, "02d"), sep=":")

print ()
