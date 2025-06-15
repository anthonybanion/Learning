# @brief:   login system
# @detail: we use the [ ] notation and operators to compare strings
# @file: login.sh
# @date: 21/05/2024
# @version: 1.0 

# /bin/bash

echo "Enter your username"
read username
echo "Enter your password"
read password

while [ $username != "admin" ] || [ $password != "admin" ]; do    
    echo "Invalid username or password"
    sleep 1
    clear
    echo "Enter your username"
    read username
    echo "Enter your password"
    read password
done
    if [ $username == "admin" ] && [ $password == "admin" ]; then
        echo "Welcome $username"
    else
        echo "Invalid username or password"
    fi