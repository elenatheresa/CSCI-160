'''
elena corpus
csci 160 : 5-7
part 2 : progam that uses your credits to figure out what year I am,
how many credits to graduate,
and how many semesters left
'''

num = (input("Enter the number of credits you have earned already: "))

#finding what year I am
if int(num) <= 23:
    print("Current Freshman")
elif int(num) > 23 and int(num) <= 59:
    print("Current Sophmore")
elif int(num) > 59 and int(num) <= 89:
    print("Current Junior")
else :
    print("Current Senior")

#after this semester what year I am
num2= (input("Enter the number of credits you are taking now: "))
sum = int(num) + int(num2)

if int(sum) <= 23:
    print("Current Freshman")
elif int(sum) > 23 and int(sum) <= 59:
    print("Current Sophmore")
elif int(sum) > 59 and int(sum) <= 89:
    print("Current Junior")
else :
    print("Current Senior")
    
#minumum number of addition credits needed to graduate
sum = (120 - (int(num) + int(num2)))
print("I will now need", sum, "to graduate")

#how many sememsters left
sum = ((120 - (int(num) + int(num2))) // 17)
print("I have", sum, "semesters left")
