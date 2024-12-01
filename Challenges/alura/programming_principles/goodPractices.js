/*Brief: good practices exercises
 *Location: Programming logic: Dive into programming with javasript/ Good practices
 *Date: 20/06/2024*/


//1. Create a program that uses console.log to display a welcome message.
let message = "Welcome to our website!";
console.log(message);

//2. Create a variable called "name" and give it your name. Then, use console.log to display 
//the message "Hello, [your name]!" in the browser console.
let name = "Anthony";
console.log("Hello, " + name + "!");    

//3. Create a variable called "name" and give it your name. Then, use alert to display the 
//message "Hello, [your name]!"
name = "Anthony";
alert("Hello, " + name + "!");

//4. Use prompt and ask the following question: What is the programming language you like 
//the most? Then, it stores the answer in a variable and displays the answer in the browser console.
let programmingLanguage = prompt("What is the programming language you like the most?");
console.log(programmingLanguage);

//5. Create a variable called "value1" and another called "value2", assigning them numerical values 
//of your choice. Then, it makes the sum of these two values and stores the result in a third variable 
//called "result". Use console.log to display the message "The sum of [value1] and [value2] equals [result]." 
//in the console.
let value1 = 10;
let value2 = 20;
let result = value1 + value2;
console.log("The sum of " + value1 + " and " + value2 + " equals " + result + ".");

//6. Create a variable called "value1" and another called "value2", assigning them numerical values of 
//your choice. Then, it subtracts these two values and stores the result in a third variable called "result." 
//Use console.log to display the message "The difference between [value1] and [value2] equals [result]." in the console.
value1 = 20;
value2 = 10;
result = value1 - value2;
console.log("The difference between " + value1 + " and " + value2 + " equals " + result + ".");

//7. Ask the user to enter their age with prompt. Based on the age entered, it uses an if to check if the 
//person is older or younger and displays an appropriate message on the console.
let age = prompt("How old are you?");
if (age >= 60){
    console.log("You are older.");
} else {
    console.log("You are younger.");
} 

//8. Create a variable "number" and prompt for a value. Then, check if it's positive, negative, or zero using 
//an if-else and display the corresponding message.
let number = prompt("Enter a number: ");
if (number > 0){
    console.log("Positive number.");
} else if (number < 0){
    console.log("Negative number.");
} else {
    console.log("Zero.");
}

//9. Use a while loop to display the numbers 1 through 10 on the console.
let counter = 1;
while (counter <= 10){
    console.log(counter);
    counter++;
}

//10. Create a "note" variable and assign it a numeric value. It uses an if-else to determine if the grade is 
//greater than or equal to 7 and displays "Pass" or "Fail" in the console.
let note = 8;
if (note >= 7){
    console.log("Pass");
}else {
    console.log("Fail");
}

//11. Use Math.random to generate any random number and display that number in the console.
let randomNumber = Math.random();
console.log(randomNumber);

//12. Use Math.random to generate an integer between 1 and 10 and display that number in the console.
randomNumber = (Math.random() * 10) +1;
console.log(randomNumber);

//13. Use Math.random to generate an integer between 1 and 1000 and display that number in the console.
randomNumber = (Math.random() * 1000) +1;
console.log(randomNumber);
