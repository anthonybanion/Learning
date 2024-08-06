/*Brief: more Functions exercises
 *Location: Programming logic: exploring functions and lists / restarting the game
 *Date: 03/08/2024*/


const LOWER_LIMIT = 18.6;
const UPPER_LIMIT = 24.9;
let weight = parseFloat(prompt("Enter your weight: "));
let height = parseFloat(prompt("Enter your height: "));

//1. Create a function that calculates a person's body mass index (BMI) from their 
//height in meters and weight in kilograms, which will be received as parameters. 
function calculateBMI(weight, height) {
    const bmi = (weight / (height**2));  // Calculate BMI using the formula: BMI = weight / (height^2)
    console.log(bmi);

    if (bmi < LOWER_LIMIT) {   // Determine the BMI category
        return "Underweight";
    } else if (bmi >= LOWER_LIMIT && bmi < UPPER_LIMIT) {
        return "Normal";
    } else {
        return "Overweight";
    }
}

const result = calculateBMI(weight, height);
console.log(`BMI Category: ${result}`);

//2. Create a function that calculates the value of the factorial of a number 
//passed as a parameter. 
let number = parseInt(prompt("Enter a number"));
let counter = 1;
function factorial(number){
    for(i=1; i<=number;i++){
        counter = counter*i;
    }
return counter;
}
alert(factorial(number));

//3. Create a function that converts a value in dollars, passed as a parameter, 
//and returns the equivalent value in reais (Brazilian currency, if you want 
//you can do it with the value of the dollar in your country). For this, 
//consider the dollar rate equal to R$4.80. 
const PRICE_OF_DOLLAR = 4.8;
const dollar = prompt("Enter the dollar value: ");
const real = PRICE_OF_DOLLAR;
function convertDollar(dollar){
    return dollar * real;
}
alert("the vale of the dollar is: " + convertDollar(dollar));


//4. Create a function that displays the area and perimeter of a rectangular room, 
//using the height and width to be provided as parameters. 
height = parseFloat(prompt("Enter the height: "));
width = parseFloat(prompt("Enter the width: "));
function calculateAreaPerimeter(height, width){
    const area = height * width;
    const perimeter = 2 * (height + width);
    return `Area: ${area}, Perimeter: ${perimeter}`;
}
alert(calculateAreaPerimeter(height, width));

//5. Create a function that displays the area and perimeter of a circular room, 
//using its radius that will be provided as a parameter. Consider Pi = 3.14.
const PI = 3.14;
const radius = parseFloat(prompt("Enter the radius: "));
function calculateAreaPerimeterCircle(radius){
    const area = Math.round(PI * radius**2);
    const perimeter = Math.round( 2 * PI * radius);
    return `Area: ${area}, Perimeter: ${perimeter}`;
}
alert(calculateAreaPerimeterCircle(radius));

//6. Create a function that displays the multiplication table of a number given as a parameter.
number = parseInt(prompt("Enter a number: "));
function multiplicationTable(number){
    for(i=1; i<=10; i++){
        console.log(`${number} x ${i} = ${number * i}`);
    }
}

multiplicationTable(number);