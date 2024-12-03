/*Brief: Write a program that generates a random number between 1 and 100. 
        The user must try to guess it.
 Date: 03/12/2024
 Version: 1.0
*/

using System;

// Generate a random number between 1 and 100
Random random = new Random();
int secretNumber = random.Next(1, 101);

Console.WriteLine("Welcome to the Number Guessing Game!");
Console.WriteLine("You have 5 attempts to guess a number between 1 and 100.");

int attempts = 0;
bool guessed = false;

// Loop for up to 5 attempts
while (attempts < 5 && !guessed)
{
    Console.Write($"Attempt {attempts + 1}: Enter your guess: ");
    string input = Console.ReadLine();

    // Try to parse the input into a number
    if (int.TryParse(input, out int userGuess))
    {
        attempts++;
        if (userGuess == secretNumber)
        {
            Console.WriteLine($"Congratulations! You guessed the secret number ({secretNumber}) in {attempts} attempts.");
            guessed = true;
        }
        else if (userGuess < secretNumber)
        {
            Console.WriteLine("The number is higher.");
        }
        else
        {
            Console.WriteLine("The number is lower.");
        }
    }
    else
    {
        Console.WriteLine("Please enter a valid number.");
    }
}

if (!guessed)
{
    Console.WriteLine($"Sorry, you've run out of attempts. The secret number was: {secretNumber}");
}

Console.WriteLine("Thanks for playing!");
