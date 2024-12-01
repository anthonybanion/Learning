//brief: creating user and password
//date: 01/12/2024
//Version: 1.0

#include <stdio.h>
#include <string.h>
#include <stdbool.h>

void getInput(char *prompt, char *input, int size) {
    printf("%s", prompt);
    fgets(input, size, stdin);
    input[strcspn(input, "\n")] = '\0'; // Remove newline character
}

bool authenticate(const char *username, const char *password) {
    return strcmp(username, "admin") == 0 && strcmp(password, "admin") == 0;
}

int main() {
    char username[50];
    char password[50];

    getInput("Enter username: ", username, sizeof(username));
    getInput("Enter password: ", password, sizeof(password));

    if (authenticate(username, password)) {
        printf("Welcome to the application\n");
    } else {
        printf("Error: Invalid username or password\n");
    }

    return 0;
}