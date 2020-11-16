'''
Elena Corpus
CSCI 160
Tuesday 5-7 pm
asking the user what kind of shape they wish to draw, either rectangle or triangle
'''

shape = input("Choose between rectangle or triangle: ")
rectangle = 'rectangle' 
triangle = 'triangle'

if shape == rectangle: 
    print("Enter width: ")
    width = int(input())
    print("Enter height: ")
    height = int(input())

    for i in range(height):
        if i in[0]:
            print("* "*(width))
        elif i in[(height-1)]:
            print("* "*(width))
        else:
            print("*"+"  "*(width-2)+" *")

elif shape == triangle:
    print("Enter height: ")
    height = int(input())

    for i in range(1, height + 1):
       print("*" * i)
