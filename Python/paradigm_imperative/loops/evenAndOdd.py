#Brief: Program that prints even and odd numbers
#statement:
#- Ask the user for an integer
#- Print all its smaller numbers
#- Report whether each number is even or odd
#Date: 20/08/2024
#Version: 1.0


number = int(input("Enter a number: "))
for i in range(1,number+1):
    if i%2==0:
        print(i,"It is even")
    else:
        print(i,"It is odd")

