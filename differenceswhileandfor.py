'''
Differences between while loop and for loop

While loop

1) While loops depend on the condition to perform the loop. if the condition is true,
   the while loop excutes the operations else it will terminate

2) While loops can act as for loops

For loop

1) if you know the number of iterations before, then we can use for loops.

2) for loops cannot act as while loops
'''

# print hello for 10 times using while loop
count = 1
while count < 11:
    print("hello")
    count += 1
