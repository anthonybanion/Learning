//Brief: A simple program that adds two numbers using a function
//Date: 01/12/2024
//Version: 1.0

#include <iostream>
#include <iostream>
using namespace std;

// Function that adds two numbers
int add(int a, int b) {
    return a + b;
}

int main() {
    int num1, num2;

    // Ask the user to enter two numbers
    cout << "Enter the first number: ";
    cin >> num1;
    cout << "Enter the second number: ";
    cin >> num2;

    // Call the add function and display the result
    int result = add(num1, num2);
    cout << "The sum of " << num1 << " and " << num2 << " is: " << result << endl;

    return 0;
}