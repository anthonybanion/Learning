/*Brief: functions exercises
 *Location : Programming logic: exploring functions and lists / Interacting with HTML
 *Date: 20/06/2024 
*/


//1. Download the project.
//2. Change the content of the h1 tag with document.querySelector and assign the following text: "Challenge Time".
function showMassage(element, texto){  
    let elementHtml = document.querySelector(element);  //Select the element
    elementHtml.innerHTML = texto;  //Insert a massage in the element
}
showMassage("h1", "Challenge Time");

//3. Create a function that displays the message "The button was clicked" in the console whenever the "Console" button is pressed.
function clicked(){
    showMassage("p", "The button Console was clicked");
}

//4. Create a function that runs when the "prompt" button is clicked, asking for the name of a city in Brazil. 
//Then, display an alert with the message by concatenating the response with the text: "I was in {city} and 
//I remembered you".
function remember(){
    let city = prompt("Enter a name of a city in Brazil: ");
    alert(`I was in ${city} and I remembered you`);
}

//5. Create a function that displays an alert with the message: "I love JS" whenever the "Alert" button is pressed.
function preferredLanguage(){
    alert("I love JavasScript!");
}


//6. When the "sum" button is clicked, it asks for 2 numbers and displays the result of the sum in an alert.
function sum(){
    number1 = parseInt(prompt("Enter the first number: "));
    number2 = parseInt(prompt("Enter the second number: "));
    alert("The sum is : " + (number1 + number2));
}