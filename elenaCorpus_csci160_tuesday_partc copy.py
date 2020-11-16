'''
Elena Corpus
CSCI 160
Tuesday 5-7 pm
writing a program that asks for the length of a line using astriks 
'''

#for loops 
line_length = int(input("Enter the length of line you wish to draw: "))

for line_length in range(1,line_length + 1):
    line_length = "*"
    print(line_length, end=' ')

#while loops 
print()

print("with while loop")
line_length = int(input("Enter the length of line you wish to draw: "))
count = 1

while count <= line_length:
    print("*", end=' ')
    count = count + 1 

