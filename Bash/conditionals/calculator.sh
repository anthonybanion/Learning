# brief: simple calculator that performs the four basic mathematical operations. 
# detail: used the case statement to select the operation to be performed.
# file: calculator.sh
# date: 21/05/2024
# verion: 0.1

#! /bin/bash

echo "Enter the first number: "
read number1
echo "Enter the second number: "
read number2
clear
echo "1: (+) sum"
echo "2: (-) subtration"
echo "3: (*) multiplication"
echo "4: (/) division"
echo "Enter the mathematical operation"
read operation
case $operation in
    1) 
        echo "The sum is $((number1 + nmber2))"
	;;
    2) 
         echo "The subration is: $((number1 - number2))"
        ;;
    3) 
        echo "The multiplication is: $((number1 * number2))"
        ;;
    4)  
        if ((number2 == 0)) then
            echo "wrong  denominator "
        else
            echo "Te division is: $((number1 / number2))"
        fi
        ;;
    *) 
        echo "incorrected"
        ;;
esac
