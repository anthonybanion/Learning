# brief: the program tells you what stage of life you are in. 
# detail: use of double parentecis for logical expressions
# file: life_stages.sh
# date: 21/05/2024
# version: 1.0

#! /bin/bash

echo "LIFE STAGE"
echo ""
echo "Enter you age"
read age
if ((age > 0)) && ((age <= 12)) then
    echo "you are a child"
elif ((age > 12)) && (( age <= 18)) then
    echo "you are a adolescent"
elif ((age > 18)) && (( age <= 21)) then
    echo "you are a young adult"
elif ((age > 21)) && (( age <= 61)) then
    echo "you are a older adult"
elif ((age > 61)) && (( age < 99)) then
    echo "you are a grandparent"
else
    echo "incorret age"
fi


