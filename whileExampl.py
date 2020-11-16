'''
Initial while loop

Counting from counter (1) to the target value (user input)
'''

counter = 1
target = int ( input ("How high should the program count? "))

while counter <= target: #pretest loop
   #if counter % 100000 == 0:
   print (counter)

   counter = counter + 1

print ("The loop executed", target, "times")
