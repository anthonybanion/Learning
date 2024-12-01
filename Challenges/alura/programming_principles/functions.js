/*Brief: Functions exercises
 *Location: Programming logic: exploring functions and lists / Functions
 *Date: 20/06/20204*/

//1. Create a function that displays "Hello, world!" on the console. 
function greet(){
    console.log("Hello Wordl!");
}
greet();

//2. Create a function that takes a name as a parameter and returns "Hello, [name]!" on the console.
function personalizedGreeting(){
    let name = prompt("Enter your name: ");
    alert(`Hello, ${name}!`);
}
personalizedGreeting();


//3. Create a function that takes a number as a parameter and returns double that number. 
function doubleNumber(){
    let number = parseInt(prompt("Enter a number: "));
    alert(number*2);
}
doubleNumber();
//4. Create a function that receives three numbers as parameters and returns their average. 
position = ["first","second", "third"];
console.log(position);
let sum = 0;
function average(){
    for (i=0; i<=2; i++){
        number = parseInt(prompt(`Enter the ${position[i]} number: `));
        sum = sum + number;
    }
    return (sum / 3);
}
alert(average());

//5. Create a function that receives two numbers as parameters and returns the largest of them. 
function largestNumber(){
    let numberOne = parseInt(prompt(`Enter the first number: `)); 
    let numberTwo = parseInt(prompt(`Enter the second number: `)); 
    if (numberOne > numberTwo){
        alert("the largest number is: " + numberOne);
    } else if (numberOne < numberTwo){
        alert("the largest number is: " + numberTwo);
    } else{
        alert("the numbers are the same");
    }
}
largestNumber()

//6. Create a function that takes a number as a parameter and returns the result of multiplying that 
//number by itself.
function multiplyByItself(){
    number = parseInt(prompt("Enter a number: "));
    alert(number * number);
}
multiplyByItself();