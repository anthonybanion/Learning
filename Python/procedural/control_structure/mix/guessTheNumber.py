#Brief: Guess the number
#Guess the number
#- The program has a random number between 1 and 100
#- The user has to guess the number
#- The program tells the user if the number is higher or lower
#- Number of attempts: 10 times
# Date: 20/08/2020
# Version 1.0


import random as rd

LOWER_LIMIT = 1
HIGH_LIMIT = 100
RANDON_NUMBER = rd.randint(LOWER_LIMIT, HIGH_LIMIT)  
ATTEMPTS = 10

user_number = int(input("Guess a number between 1 and 100: "))

if user_number < LOWER_LIMIT or user_number > HIGH_LIMIT:
    print("The number is out of range")
else:
    for i in range(ATTEMPTS):
        if user_number > RANDON_NUMBER:
            print("The number is less")
        elif user_number < RANDON_NUMBER:
            print("The number is greater")
        else:
            print("Congratulations, you guessed the number")
            break
        user_number = int(input("Guess a number between 1 and 100: "))
    print("You have run out of attempts")



