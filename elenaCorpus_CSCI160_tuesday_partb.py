'''
Elena Corpus
CSCI 160
Tuesday 5-7 pm
writing a program that computes a small, single value multiplication table
'''

num = int(input("Enter a value between 1 - 10: "))
if (num > 1) and (num < 10):

#labeling 
    if num == 1:
        print("Multiplication table for 1")
    elif num == 2:
        print("Multiplication table for 2")
    elif num == 3:
        print("Multiplication table for 3")
    elif num == 4:
        print("Multiplication table for 4")
    elif num == 5:
        print("Multiplication table for 5")
    elif num == 6:
        print("Multiplication table for 6")
    elif num == 7:
        print("Multiplication table for 7")
    elif num == 8:
        print("Multiplication table for 8")
    elif num == 9:
        print("Multiplication table for 9")
        
#multiplication table         
    for i in range(1,11):
        print(num, 'x', i, '=', num * i)

else:
    print("Error: Number must be between 1 - 10")

                
    
