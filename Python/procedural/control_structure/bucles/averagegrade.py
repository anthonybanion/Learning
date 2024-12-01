#Brief: This program calculates the average of the grades
# statement: Averagegrade
#- Prompts the user for the number of grades to enter
#- Enter grades by keyboard
#- calculates the average of the grades
#- inform if I approve or disapprove, minimum grade 60
# Date: 20/08/2024
# Version: 2.0
#- Commit: use list and for loop

# MINIMUN_GRADE=60

# grades=[]
# number_of_grades = int(input("Enter the number of grades you are going to enter? "))

# for i in range(number_of_grades):
#     grades.append(float(input("Enter the grades: ")))

# average = sum(grades)/number_of_grades
# print("The averagegrade : ",average.__round__(2))

# if average>=MINIMUN_GRADE:
#     print("Approved")
# else:
#     print("Disapproved")

#.................
# amount=int(input("Enter the number of course you are going to enter? "))
# course=[]
# sum=0

# for i in range(amount):
#     course.append(str(input("Enter the course: ")))
#     note=float(input("Enter the note: "))
#     sum+=note

# average=sum/amount

# print("The average is: ",average.__round__(2))

course=[]
note=[]
amount = int(input("Enter the number of course you are going to enter? "))
sum = 0

for i in range(amount):
    course.append(str(input("Enter the course: ")))
    note.append(float(input("Enter the note: ")))
    sum += note[i]

average=sum/amount
print("The average is: ",average.__round__(2))
