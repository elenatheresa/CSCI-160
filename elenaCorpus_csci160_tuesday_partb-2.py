'''
Elena Corpus
CSCI 160
Tuesday 5-7
writing a program that asks for integer values until the user enters 0
'''

user_num = float(input("Enter a value: "))
positive_value = 0
negative_value = 0
count_positive = 0
count_negative = 0

while user_num != 0:
    if user_num > 0:
        positive_value = positive_value + user_num
        count_positive = count_positive + 1
    elif user_num < 0 :
        negative_value = negative_value + user_num
        count_negative = count_negative + 1 
    user_num = float(input("Enter a value: "))

if count_positive != 0:
    average_positive = positive_value / count_positive               
    print("Average of positive values: ", format(average_positive, ".2f"))
else:
    print("No positive values have been entered")
    
if count_negative != 0:
    average_negative = negative_value / count_negative               
    print("Average of negative values: ", format(average_negative, ".2f"))
else:
    print("No negative values have been entered")
