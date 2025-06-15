# @brief:  survey to know our personality.
# @detail: we use the [ ] notation 
# @file: survey.sh
# @date: 21/05/2024
# @version: 0.1




#! /bin/bash

echo "SURVEY"
echo "What is your name?"
read name
echo "How old are you?"
read age
clear
echo "What is your favorite color?"
echo "1: red"
echo "2: blue"
echo "3: green"
echo "4: yellow"
echo "5: black"
echo "6: white"
read option1
case $option1 in
    1) 
        echo "You selected red"
        color="red"
        ;;
    2) 
        echo "You selected blue"    
        color="blue"
        ;;
    3) 
        echo "You selected green"
        color="green"
        ;;
    4) 
        echo "You selected yellow"
        color="yellow"
        ;;
    5) 
        echo "You selected black"
        color="black"
        ;;
    6) 
        echo "You selected white"
        color="white"
        ;;
    *) 
        echo "You selected an invalid option"
        ;;
esac
clear
echo "what is your favorite animal?"
echo "1: dog"
echo "2: cat"
echo "3: bird"
echo "4: fish"
echo "5: rabbit"
echo "6: snake"
read option2
case $option2 in
    1) 
        echo "You selected dog"
        animal="dog"
        ;;
    2) 
        echo "You selected cat"
        animal="cat"
        ;;
    3) 
        echo "You selected bird"
        animal="bird"
        ;;
    4) 
        echo "You selected fish"
        animal="fish"
        ;;
    5) 
        echo "You selected rabbit"
        animal="rabbit"
        ;;
    6) 
        echo "You selected snake"
        animal="snake"
        ;;
    *) 
        echo "You selected an invalid option"
        ;;
esac
clear
echo " $name, $age years old: "
if [ $color == "red" ] && [ $animal == "dog" ]; then
    echo "You are a passionate person"
elif [ $color == "blue" ] && [ $animal == "cat" ]; then
    echo "You are a calm person"
elif [ $color == "green" ] && [ $animal == "bird" ]; then
    echo "You are a free person"
elif [ $color == "yellow" ] && [ $animal == "fish" ]; then
    echo "You are a happy person"
elif [ $color == "black" ] && [ $animal == "rabbit" ]; then
    echo "You are a mysterious person"
elif [ $color == "white" ] && [ $animal == "snake" ]; then
    echo "You are a dangerous person"
else
    echo "You are a normal person"
fi