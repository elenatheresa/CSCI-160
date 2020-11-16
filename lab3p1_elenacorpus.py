'''
Elena Corpus
Lab Sect : Tues 5-7pm
Inputing int and outputing English words
'''

'''
number = int(input("enter number to print: "))
num2words = str({1:'One',2:'Two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',
              20: 'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy',
               80:'eighty', 90:"ninty"})


if (str(num2words) > 21) and (str(num2words) < 100) :
    print("the number is", num2words)
else:
    print("Number Out of Range")

'''
'''
number = int(input("enter number to print: "))
if(int(number) >= 20) and (int(number) <= 99):
    print("The number is ", number)
else:
    print("number out of range")

'''

num = int(input("enter number to print: "))

if int(num) == 20 :
    print("the number is twenty")
elif int(num) == 21 :
    print("the number is twenty-one")
elif int(num) == 22 :
    print("the number is twenty-two")
elif int(num) == 23:
    print("the number is twenty-three")
elif int(num) == 24 :
    print("the number is twenty-four")
elif int(num) == 25 :
    print("the number is twenty-five")
elif int(num) == 26:
    print("the number is twenty-six")
elif int(num) == 27 :
    print("the numebr is twenty-seven")
elif int(num) == 28 :
    print("the number is twenty-eight")
elif int(num) == 29:
    print("the number is twenty-nine")
elif int(num) == 30 :
    print("the number is thirty")
elif int(num) == 31 :
    print("the number is thirty-one")
elif int(num) == 32:
    print("the number is thirty-two")
elif int(num) == 33 :
    print("the numebr is thirty-three")
elif int(num) == 34 :
    print("the number is thirty-four")
elif int(num) == 35 :
    print("the number is thirty-five")
elif int(num) == 36 :
    print("the number is thirty-six")
elif int(num) == 37 :
    print("the number is thirty-seven")
elif int(num) == 38:
    print("the number is thirty-eight")
elif int(num) == 39 :
    print("the numebr is thirty-nine")
elif int(num) == 40 :
    print("the number is forty")
elif int(num) == 41:
    print("the number is forty-one")
elif int(num) == 42 :
    print("the numebr is forty-two")
elif int(num) == 43 :
    print("the number is forty-three")
elif int(num) == 44:
    print("the number is forty-four")
elif int(num) == 45 :
    print("the numebr is forty-five")
elif int(num) == 46 :
    print("the number is forty-six")
elif int(num) == 47:
    print("the number is forty-seven")
elif int(num) == 48 :
    print("the number is forty-eight")
elif int(num) == 49 :
    print("the number is forty-nine")
elif int(num) == 50 :
    print("the number is fifty")
elif int(num) == 51 :
    print("the number is fifty-one")
elif int(num) == 52 :
    print("the number is fifty-two")
elif int(num) == 53:
    print("the number is fifty-three")
elif int(num) == 54 :
    print("the number is fifty-four")
elif int(num) == 55 :
    print("the number is fifty-five")
elif int(num) == 56:
    print("the number is fifty-six")
elif int(num) == 57 :
    print("the number is fifty-seven")
elif int(num) == 58 :
    print("the number is fifty-eight")
elif int(num) == 59:
    print("the number is fifty-nine")
elif int(num) == 60 :
    print("the numebr is sixty")
elif int(num) == 61 :
    print("the number is sixty-one")
elif int(num) == 62:
    print("the number is sixty-two")
elif int(num) == 63 :
    print("the numebr is sixty-three")
elif int(num) == 64 :
    print("the number is sixty-four")
elif int(num) == 65 :
    print("the number is sixty-five")
elif int(num) == 66 :
    print("the numebr is sixty-six")
elif int(num) == 67 :
    print("the number is sixty-seven")
elif int(num) == 68:
    print("the number is sixty-eight")
elif int(num) == 69 :
    print("the numebr is sixty-nine")
elif int(num) == 70 :
    print("the number is seventy")
elif int(num) == 71:
    print("the number is seventy-one")
elif int(num) == 72 :
    print("the numebr is seventy-two")
elif int(num) == 73 :
    print("the number is seventy-three")
elif int(num) == 74:
    print("the number is seventy-four")
elif int(num) == 75 :
    print("the numebr is seventy-five")
elif int(num) == 76 :
    print("the number is seventy-six")
elif int(num) == 77:
    print("the number is seventy-seven")
elif int(num) == 78 :
    print("the numebr is seventy-eight")
elif int(num) == 79 :
    print("the number is seventy-nine")
elif int(num) == 80 :
    print("the number is eighty")
elif int(num) == 81 :
    print("the number is eighty-one")
elif int(num) == 82:
    print("the number is eighty-two")
elif int(num) == 83 :
    print("the number is eighty-three")
elif int(num) == 84 :
    print("the number is eighty-four")
elif int(num) == 85 :
    print("the number is eighty-five")
elif int(num) == 86 :
    print("the number is eighty-six")
elif int(num) == 87 :
    print("the number is eighty-seven")
elif int(num) == 88:
    print("the number is eighty-eight")
elif int(num) == 89 :
    print("the number is eighty-nine")
elif int(num) == 90 :
    print("the number is ninety")
elif int(num) == 91:
    print("the number is ninety-one")
elif int(num) == 92 :
    print("the numebr is ninety-two")
elif int(num) == 93 :
    print("the number is ninety-three")
elif int(num) == 94:
    print("the number is ninety-four")
elif int(num) == 95 :
    print("the numebr is ninety-five")
elif int(num) == 96 :
    print("the number is ninety-six")
elif int(num) == 97:
    print("the number is ninety-seven")
elif int(num) == 98 :
    print("the number is ninety-eight")
elif int(num) == 99 :
    print("the number is ninety-nine")
else :
    print("the number is not withint a valid range")






