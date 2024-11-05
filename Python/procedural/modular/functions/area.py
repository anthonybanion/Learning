# Title: Area
# Staments:
#- create a function that calculates the area of ​​the triangle
# Date: 21/08/2024
# Version: 1.0


base = float(input('Enter the base of the triangle: '))
height = float(input('Enter the height of the triangle: '))

def area(base, height):
    return (base * height) / 2


if base < 0 or height < 0:
    print('The base and height must be greater than 0')
else:
    print(area(base, height)) 