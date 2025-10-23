/* @brief: This script generates a random number between 1 and 10
and asks the user to guess it.
* @details: The user only have 3 attempts.
* @version: 1.0
* @date: 12/07/2024*/

let randomNumber = Math.floor(Math.random() * 10) + 1;  //Random number between 1 and 10
let userNumber = 0;
let attempts = 1;

while(userNumber != randomNumber){
    userNumber = prompt("Enter a value between 1 and 10: ");

    if (userNumber == randomNumber){
        alert(`Congratulations! you guessed the number,
            the number is: ${userNumber}.
            Number of attempts: ${attempts}`);
    }else{
        if (userNumber > randomNumber){
            alert(`Sorry, the number is lower than ${userNumber}`);
        }else{
            alert(`Sorry, the number is higher than ${userNumber}`);
        }
        attempts++;
        if (attempts > 3){
            alert(`Sorry, you have reached the maximum number of attempts.
                The number was ${randomNumber}`);
            break;
        }
    }
}