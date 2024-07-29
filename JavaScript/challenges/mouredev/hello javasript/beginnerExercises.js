/*Brief: Data types, operators and strings
*Detal: Class 2 on video | 17/07/2024
*Date: 29/072024 
*Link: https://www.twitch.tv/videos/2200149072?t=00h08m02s
*/
// 1. Write a comment on one line 
    alert("This is a one line comment: Hello JavaScript");

// 2. Write a comment on several lines 
    alert("This is a multi-line comment: \n 1. HTML \n 2. CSS \n 3. JavaScript");

// 3. Declare variables with values ​​associated with all primitive type data 
    let number = 10;
    let string = "Hello JavaScript";
    let boolean = true;
    let undefinedVar = undefined;
    let nullVar = null;

// 4. Print the value of all variables through the console 
    console.log(number);
    console.log(string);
    console.log(boolean);
    console.log(undefinedVar);
    console.log(nullVar);

// 5. Print the type of all variables through the console 
    console.log(typeof number);
    console.log(typeof string);
    console.log(typeof boolean);
    console.log(typeof undefinedVar);
    console.log(typeof nullVar);

// 6. Next, modify the values ​​of the variables with others of the same type 
    number = 20;
    string = "Hello World";
    boolean = false;
    undefinedVar = null;
    nullVar = undefined;

    console.log("Values of the variables have been modified");
    console.log(number);
    console.log( string);
    console.log(boolean);
    console.log(undefinedVar);
    console.log(nullVar);

// 7. Next, modify the values ​​of the variables with others of a different type 
    number = "Hello" + 100;  
    string = Number((10 + 1) + "100");  
    boolean = null;
    undefinedVar = parseFloat("10.10");  
    nullVar = true;

    console.log("Values of the variables have been modified");
    console.log(number);
    console.log(typeof number);  // The result is "Hello100" type of string
    console.log( string);
    console.log(typeof string);  // The result is 10100 type of number
    console.log(boolean);
    console.log(typeof boolean);
    console.log(undefinedVar);
    console.log(typeof undefinedVar);  // The result is 10.10 type of number
    console.log(nullVar);
    console.log(typeof nullVar);

// 8. Declare constants with values ​​associated with all primitive data types 
    const numberConst = 10;
    const stringConst = "Hello JavaScript";
    const booleanConst = true;
    const undefinedConst = undefined;
    const nullConst = null;

    console.log(numberConst);
    console.log(stringConst);
    console.log(booleanConst);
    console.log(undefinedConst);
    console.log(nullConst);
    

// 9. Next, modify the values ​​of the constants 
    // numberConst = 20;
    // stringConst = "Hello World";
    // booleanConst = false;
    // undefinedConst = null;
    // nullConst = undefined;

// 10. Comment the lines that produce some type of error when executed
    // The lines that produce an error are lines 79 to 83
    // The error is: Uncaught TypeError: Assignment to constant variable.
    // becasue we are trying to change the value of a constant variable