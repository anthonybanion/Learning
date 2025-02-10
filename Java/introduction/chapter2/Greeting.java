/*Brief: Write a program that asks the user's name, 
        and then greets the user by name.
 *Detail: Exercise 2.3
 *Source: https://math.hws.edu/eck/cs124/javanotes9-swing/c2/ex3-ans.html
 *Date: 09/02/2025
 *Version: 1.0
*/

package Java.introduction.chapter2;
import java.util.Scanner;

public class Greeting {
    
    public static void main(String[] args) {
    
        Scanner stdin = new Scanner( System.in );
    
        String usersName;      // The user's name, as entered by the user.
        String upperCaseName;  // The user's name, converted to upper case letters.
        
        System.out.print("Please enter your name: ");
        usersName = stdin.nextLine();
        
        upperCaseName = usersName.toUpperCase();
        
        System.out.println("Hello, " + upperCaseName + ", nice to meet you!");
    
        stdin.close();
    }  // end main()
 
}  // end class