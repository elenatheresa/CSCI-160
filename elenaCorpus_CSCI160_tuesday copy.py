'''
Elena Corpus
CSCI 160
Tuesday 5 - 7pm
writing a program that will continue to ask a user to enter a temperature
in Celsius until the user enters 800
'''

temp = int(input("Please enter the temperature in Celcius: "))
fahrenheit = 0
ave_temp = 20
extremely_cold = 0
cold = 0
warm = 0
extremely_hot = 0

while temp != 800:
        if temp <= -25:
            extremely_cold = extremely_cold + 1
            print("The temperature entered is Extremely Cold")
            
        elif (temp >= -24) and (temp <= 10):
            cold = cold + 1
            print("The temperature entered is Cold")
            
        elif (temp >= 11) and (temp <= 32):
            warm = warm + 1
            print("The temperature entered is Warm")
            
        elif temp >= 33:
            extremely_hot = extremely_hot + 1
            print("The temperature entered is Extremely hot")
            
        ave_temp = abs(ave_temp - temp)
        print("the temperature entered is ", ave_temp,"from the average temperature")
        farenheit = temp * 1.8 + 32
        print("the temperature is ",farenheit, "in Fahrenheit")

        print()

        temp = int(input("Please enter the temperature in Celcius: "))       

print("You had ", extremely_cold, "Extremely cold location(s)")
print("You had ", cold, "Cold location(s)")
print("You had ", warm, "Warm locations(s)")
print("You had ", extremely_hot, "Extremely warm location(s)")

       


