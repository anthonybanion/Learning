#Brief: General solution in fuction
#Date: 13/12/2024
#Version: 1.0

import math
def generalSolution(a,b,c):
    delta= b*2-4*a*c
    print(delta)
    squareRoot= math.sqrt(delta)
    print(squareRoot)
    numerator = -b + delta
    print(numerator)
    denominator = 2*a
    print(denominator)
    root= numerator / denominator
    print(root)
    return root;

print(generalSolution(1,12,1))