/*brief: This file is about the type of data in JavaScript.
 *Observation: Most data types in JavaScript are objects
 *date: 28/07/2024
*version: 1.0*/


// type of date string
let name = "John";
alert(name); 
console.log(typeof name);   // output: string

// type of date number
let age = 25;
alert(age);
console.log(typeof age);  // output: number

// type of date boolean
let isMarried = false;
alert(isMarried);
console.log(typeof isMarried); // output: boolean

// type of date null
let car = null;
alert(car);
console.log(typeof car);  // output: object

// type of date undefined
let test;
alert(test);
console.log(typeof test);  // output: undefined  

// type of date symbol
let id = Symbol("id");
alert(id.description);
console.log(id);
console.log(typeof id);  // output: symbol

// type of date array
let fruits = ["Apple", "Orange", "Plum"];
alert(fruits);
console.log(typeof fruits);  // output: object

// type of date matrix
let matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]];
alert(matrix);
console.log(typeof matrix);  // output: object

// type of date function
function sayHi() {
  alert("Hello");
}
alert(sayHi);
console.log(sayHi);
console.log(typeof sayHi);  // output: function

// type of date set
let set = new Set([1, 2, 3, 4, 5]);
alert(set);
console.log(set);
console.log(typeof set);   // output: object

// type of date map
let map = new Map();
map.set("1", "str1");
map.set(1, "num1");
alert(map);
console.log(map);
console.log(typeof map);  // output: object

// type of date object
let user = {name: "John", lastName: "Smith"};
alert(user);
console.log(user); 
console.log(typeof user);  // output: object

//Type class
class User {
  constructor(name, lastName) {
    this.name = name;
    this.lastName = lastName;
  }
}
console.log(User);
console.log(typeof User);  // output: function

// type of date date
let date = new Date();
alert(date);
console.log(typeof date);  // output: object