# Login
# File: login.py
# Created: 2024-08-21
# Last Updated: 2025-06-10
# Version: 1.0.1

"""
Statement:
- the system will have a default password
- the user will enter his password
- if they match, the session starts
"""
password = "admin"
user_password = input("Enter your password: ")

while (password != user_password):
    print("Incorrect password")
    user_password = input("Entre your password:")

if password == user_password:
    print("Correct password")
