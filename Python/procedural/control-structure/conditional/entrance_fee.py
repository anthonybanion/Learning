# Brief: Entrance fee
# Staments:
#- The program must ask the user the age and show the price of the ticket 
#- If the client is under 4, enter for free
#- If you are between 4-18, you must pay 5 thousand
#- If you are over 18, you must pay 10 thousand
#- If you are over 65, enter for free
# Date: 21/08/2024
# Version: 1.0

HIGHEST_AGE_LIMIT = 99
LOWER_AGE_LIMIT = 0
UNDER_AGE = 4
TEENAGER = 18
OLD = 65


age= int(input("Enter your age: "))
if ((age < LOWER_AGE_LIMIT ) or (age > HIGHEST_AGE_LIMIT)):
    print("Data not admissible")
elif ((age < UNDER_AGE ) or (age > OLD)):
    print("Enter free")
elif ((age >= UNDER_AGE) and (age <= TEENAGER)):
    print("Pay 5 thousand")
elif ((age > TEENAGER) and (age <= OLD)):
    print("Pay 10 thousand")