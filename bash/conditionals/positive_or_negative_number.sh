# brief: whether a number is positive, negative or zero
# detail: variables within the logical expression are prefixed with “$”.  
# file: positive_or_negative_number.sh
# date: 21/05/2024
# version: 1.0

#! /bin/bash

echo "enter a number"
read number
if (($number > 0)) then
    echo "number is positive"
elif (($number < 0)) then
    echo "number is negative"
else 
    echo "number is zero"
fi 
