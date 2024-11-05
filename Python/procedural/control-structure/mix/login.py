# Title: Login
#- the system will have a default password
#- the user will enter his password
#- if they match, the session starts
# Date: 21/08/2024
# Version: 1.0

password = "admin"
user_password = input("Entre your password: ")

while (password != user_password):
    print("Incorrect password")
    user_password = input("Entre your password:")

if password == user_password:
    print("Correct password")
