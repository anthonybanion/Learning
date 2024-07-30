/*Brief: loops and attempts exercises
 *Location: Programming logic: Dive into programming with javasript/ Loops and attempts
 *Date: 14/06/2024*/ 

//1. Create a counter that starts at 1 and goes up to 10 using a 'while' loop. Show each number. 
let counter =1;
while (counter <= 10){
    console.log(counter);
    counter++;  
}

//2. Create a counter that starts at 10 and goes to 0 using a 'while' loop. Show each number. 
let counter2 = 10;
while (counter2 >=0){
    console.log(counter2);
    counter2--;
}

//3. Create a count-up schedule. Asks for a number and counts from 0 to that number using a 'while' 
//loop in the browser console.
let counter3 = 0;
let number = prompt("Enter a number: ");
while (counter3 <= number){
    console.log(counter3);
    counter3++;
}
