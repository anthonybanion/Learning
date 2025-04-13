/*Brief: This program reads the user's first name and last name,
        separated by a space.
 *Detail: Exercise 2.6
 *Source: https://math.hws.edu/eck/cs124/javanotes9-swing/c2/ex6-ans.html
 *Date: 09/02/2025
 *Version: 1.0
*/


package introduction.chapter2;
import java.util.Scanner;

public class FirstNameLastName {
    
    public static void main(String[] args) {
        Scanner stdin = new Scanner(System.in);
        String input;     // The input line entered by the user.
        int space;        // The location of the space in the input.
        String firstName; // The first name, extracted from the input.
        String lastName;  // The last name, extracted from the input.
        
        System.out.println();
        System.out.println("Please enter your first name and last name, separated by a space.");
        System.out.print("? ");
        input = stdin.nextLine();
        
        space = input.indexOf(' ');
        firstName = input.substring(0, space);
        lastName = input.substring(space+1);
        
        System.out.println("Your first name is " + firstName + ", which has "
                                  + firstName.length() + " characters.");
        System.out.println("Your last name is " + lastName + ", which has "
                                  + lastName.length() + " characters.");
        System.out.println("Your initials are " + firstName.charAt(0) + lastName.charAt(0));
        stdin.close();
    }

}