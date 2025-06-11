#Phone call duration
#File: phoneCallDuration.py
# Created: 2024-11-05
# Last Updated: 2025-06-10
#Version: 1.0.1

"""
Statement: 
Given the duration (in minutes) of a phone call, 
calculate its total cost as follows: Up to 5 minutes, 
the total cost is 0.9. Beyond 5 minutes, the total 
cost is 0.9 + 0.2 for each additional minute beyond 
the first 5 minutes.
"""
BASIC_FEE = 0.9
BASIC_DURATION = 5
PREMIUM_FEE = 1.1
total_cost = 0

duration = float(input("Enter the call duration in minutes: "))

if duration < 0:
    print("The duration cannot be negative")
    exit
else:
    if duration <= 1:
        total_cost = BASIC_FEE
        print(f"The total_cost of the call is: {total_cost}")

    elif (duration > 1) or (duration <= BASIC_DURATION):
        total_cost = BASIC_FEE * duration
        print(f"The total_cost of the call is: {total_cost.__round__(2)}")

    else:
        duration = duration - BASIC_DURATION
        total_cost = BASIC_DURATION*BASIC_FEE + (duration * PREMIUM_FEE)
        print(f"The total_cost of the call is: {total_cost.__round__(2)}")

