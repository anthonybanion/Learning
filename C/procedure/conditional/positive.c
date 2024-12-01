//Brief: Simple program shear the positive number
//Date: 01/12/2024
//Version: 1.0

#include <stdio.h>

void main() {
    int number;
    printf("Enter a number: ");
    scanf("%d", &number);

    if (number > 0) {
        printf("The number is positive\n");
    } else {
        printf("The number is not positive\n");
    }
}