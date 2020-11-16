'''
Elena Corpus
CSCI 160
Tuesday 5-7
asking user for information about the classes they are taking this semester
'''

classType = input("Enter a class (to end type quit): ")
credit = 0
grade = 0
honorPoint = 0
totalCredit = 0
honorGrade = 0
classesTaken = 0
classesAttempt = 0

while classType != "quit":
    credit = int(input("Enter the number of credits: "))
    totalCredit = credit + totalCredit
    
    grade = str(input("Enter your grade: "))
    if grade == "A":
        grade = 4
        honorGrade = grade * 4
        classesTaken = classesTaken + 1
        classesAttempt = classesAttempt + 1 
    elif grade == "B":
        grade = 3
        honorGrade = grade * 3
        classesTaken = classesTaken + 1
        classesAttempt = classesAttempt + 1 
    elif grade == "C":
        grade = 2
        honorGrade = grade * 2
        classTaken = classesTaken + 1
        classesAttempt = classesAttempt + 1 
    elif grade == "D":
        grade = 1
        honorGrade = grade * 1
        classesTaken = classesTaken + 1
        classesAttempt = classesAttempt + 1 
    elif grade == "F":
        grade = 0
        classesTaken = classesTaken + 0
        classesAttempt = classesAttempt + 1 

    
    honorPoint = grade * honorGrade 
    gpa = honorPoint / totalCredit 
    
    classType = input("Enter a class: ")

    

print("GPA:                   ", format(gpa, "1.3f"))
print("Credit attempts        ", format(totalCredit,"5d"))
print("Credits passed         ", format(totalCredit,"5d"))
print("Classes attempted      ", format(classesAttempt,"5d"))
print("Classes passed         ", format(classesTaken,"5d"))
