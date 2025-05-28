"""
Description: String manipulation examples

File: strings.py
Author: Anthony Bañon
Created: 2025-05-20
Last Updated: 2025-05-20
"""


#           ...-4-3-2-1
#          0123...    
message = 'Hello World!'
# The strings are immutable
# meaning they cannot be changed after creation.
# However, you can access their elements using indexing.

print(len(message)) # Length of the string

print('?' in message) # Check if a substring is in the string
print(message.index('!')) # Find the index of a substring
print(message.count('o')) # Count the number of occurrences of a substring

greeting = message[0:5] + ' People!' # Slice the string
print(greeting) 