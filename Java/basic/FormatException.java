/* 
 * Description: This program checks exception of type NumberFormatException.
 * File: Exeption.java
 * Create Date: 12/04/2025
 */

 package basic;
 import java.util.Scanner;


public class FormatException{
    static String value; 
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter a value");
        value =  scanner.nextLine();

        // Check if the value is a number
       try {
        // This will throw a NumberFormatException if the value is not a valid integer
            int number = Integer.parseInt(value);
            System.out.println("The number is: " + number);
        } catch (NumberFormatException e) { // This is the catch block
            // This block will execute if a NumberFormatException is thrown
            System.err.println("Caught an exception: " + e.getMessage());
        } finally {
            System.out.println("This is the finally block");
        }

        scanner.close();
    }
}