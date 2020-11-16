'''
elena corpus
csci 160
tuesday 5 -7 pm
entering a string and finding out if it is a palindrome and if it is even
or odd


user_str = input('Enter a String: ')
length_user_str = len(user_str)

while user_str != ' ' :
    reversed_str = ''
    length_user_str = len(user_str)
    for character in range(length_user_str - 1, -1, -1): # three S - start stop step
        reversed_str = reversed_str + user_str[character]
    print("Reversed String: ",reversed_str)
    
    if user_str == reversed_str:
        if length_user_str % 2 == 0:
            print('It is an even palindrome.')
        else:
            print('It is an odd palindrome.')
    else:
        print('It is not a palindrome')

    user_str = input('Enter a String: ')

'''

user_str = input('enter a string: ')
while user_str != ' ':
    reversed_str = ''
    for character in reversed(user_str):
        reversed_str += character
    print('Reversed string: ',reversed_str)
    if user_str == reversed_str:
        if len(user_str) % 2 == 0:
            print('the string is an even palindrome.')
        else:
            print('the string is an odd palindrome.')
    else:
        print('the string is not a palindrome.')

    user_str = input('enter a string: ')
