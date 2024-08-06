/*Brief: conditionals and concatenation exercises
 *Location: Programming logic: Dive into programming with javasript/ Conditional and concatenation
 *Date: 11/06/2024*/

 
//1. Asks the user what day of the week it is. If the answer is "Saturday" or "Sunday", it shows "Have a nice weekend!".
//Otherwise, it displays “Good week!?
let day = prompt("What weekday is today? ");
if ((day == "Saturday") || (day == "Sunday")){
    alert("Have a nice weekend!");
}
else{
    alert("Good week!");}

//2. Checks if a number entered by the user is positive or negative. Displays an informative alert.
let number = prompt("Enter a number: ");
if (number > 0){
    alert("The number is positive.");
}
else{
    alert("The number is negative.");
}

//3. Create a scoring system for a game. If the score is greater than or equal to 100, it displays "Congratulations, you've won!" Otherwise, it displays "Try again to win." 
let score = prompt("Enter your score: ");
if (score >= 100){
    alert("Congratulations, you've won!");
}
else{
    alert("Try again to win.");
}

//4.. Create a message that informs the user about their account balance, using a template string to include the balance value. 
let balance = prompt("Enter your acoount balance:");
alert(`Your account balance is: ${balance}`);

//5.. Asks the user to enter their name through a prompt. It then displays a welcome alert using that name.
let name = prompt("Enter your name: ");
alert(`Welcome ${name}`);