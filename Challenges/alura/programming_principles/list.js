

//1. Create an empty list called "genericlist". 
let genaricList = [];
console.log(genaricList);

//2. Create a list of programming languages ​​called "ProgrammingLanguages" with the following elements: 'JavaScript', 'C', 'C++', 'Kotlin' and 'Python'. 
let programingLanguages = ['JavaScript', 'C', 'C++', 'Kotlin', 'Python'];
console.log(programingLanguages);

//3. Add the following elements to the "ProgrammingLanguages" list: 'Java', 'Ruby' and 'GoLang'. 
programingLanguages.push('Java', 'Ruby','GoLang');
console.log(programingLanguages);

//4. Create a function that displays all the items in the "ProgrammingLanguages" list in the console. 
function showElements(programingLanguages){
    for(let i=0; i<=programingLanguages.length-1; i++ ) {
        console.log(programingLanguages[i]);
    }
}
showElements(programingLanguages);


//5. Create a function that displays all the items in the "ProgrammingLanguages" list in reverse order in the console. 
function showElementsReverse(programingLanguages){
    for(let i=programingLanguages.length-1; i>=0; i-- ) {
        console.log(programingLanguages[i]);
    }
}
showElementsReverse(programingLanguages);

//6. Create a function that calculates the average of the elements in a list of numbers. 
let numberList = [11, 10, 10, 9];
let sum = 0;
function average(numberList){
    for(let i=0; i<=numberList.length-1; i++){
        sum = sum + numberList[i];
    }
    return sum/numberList.length;
}
console.log(average(numberList));

//7. Create a function that displays the largest number and the smallest number in a list in the console.
let maximun = 0;
let minimun = numberList[0];
function maxMin(numberList){
    for(let i=0; i<=numberList.length-1; i++){
        if(numberList[i] > maximun){
            maximun = numberList[i];
        }
        if(numberList[i] < minimun){
            minimun = numberList[i];
        }
    }
    return `Maximun: ${maximun} Minimun: ${minimun}`;
}
console.log(maxMin(numberList));

//8. Create a function that returns the sum of all the elements in a list. 
 sum = 0;
function sun(numberList){
    for(let i=0; i<=numberList.length-1; i++){
        sum = sum + numberList[i];
    }
    return sum;
}
console.log(sun(numberList));

//9. Create a function that returns the position in the list where an element passed as a parameter is located, or -1 if it does not exist in the list. 
function position(numberList, element){
    for(let i=0; i<=numberList.length-1; i++){
        if(numberList[i] === element){
            return i;
        }
    }
    return -1;
}
console.log(position(numberList, 10));

//10. Create a function that receives two lists of numbers of the same size and returns a new list with the sum of the elements one by one. 
let numberList2 = [1, 2, 3, 4];
let sumList = [];
function sumElements(numberList, numberList2){
    for(let i=0; i<=numberList.length-1; i++){
        sumList.push(numberList[i] + numberList2[i]);
    }
    return sumList;
}
console.log(sumElements(numberList, numberList2));

//11. Create a function that receives a list of numbers and returns a new list with the square of each number.
let squareList = [];
function square(numberList){
    for(let i=0; i<=numberList.length-1; i++){
        squareList.push(numberList[i] * numberList[i]);
    }
    return squareList;
}
console.log(square(numberList));

