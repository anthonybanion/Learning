/*Brief: Write a program that prompts the user for an integer 
        and then prints the multiplication table of that number from 1 to 10.
  Date: 03/12/2024
  Version:1.0
*/

using System;

int number;

// Repeat until a valid (non-negative) number is entered
do
{
    Console.Write("Enter a positive number to generate its multiplication table: ");
    string input = Console.ReadLine();

    if (int.TryParse(input, out number) && number >= 0)
    {
        Console.WriteLine($"Multiplication table for {number}:");
        
        // Loop to generate the multiplication table
        for (int i = 1; i <= 10; i++)
        {
            Console.WriteLine($"{number} x {i} = {number * i}");
        }
    }
    else
    {
        Console.WriteLine("Invalid input. Please enter a positive integer.");
    }

} while (number < 0);

Console.WriteLine("Thanks for using the multiplication table generator!");
