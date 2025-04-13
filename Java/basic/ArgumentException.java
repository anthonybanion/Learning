/* Description: This program checks exception of type IllegalArgumentException.
 * File: Exeption.java
 * Create Date: 12/04/2025
 */

 package basic;

public class ArgumentException {
    public static void main(String[] args) {
        try {
            if (args.length == 0) {  // Check if no arguments are provided
                // This will throw an IllegalArgumentException if no arguments are provided
                throw new IllegalArgumentException("No arguments provided!");
            }
            System.out.println("Argument provided: " + args[0]);
        } catch (IllegalArgumentException e) {  // This is the catch block
            // This block will execute if an IllegalArgumentException is thrown
            System.err.println("Caught an exception: " + e.getMessage());
        } finally {
            // This block will always execute, regardless of whether an exception was thrown or not
            System.out.println("This is the finally block");
        }
    }
}
