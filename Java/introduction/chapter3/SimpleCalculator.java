/*Brief: This program evaluates simple expressions such as 2 + 2
 *  and 34.2 * 7.81, consisting of a number, an operator,
 *  and another number.  The operators +, -, *, / are allowed.
 *  The program will read and evaluate expressions until
 *  the user inputs a line that starts with the number 0.
 *Detail: Exercise 3.3
 *Source: https://math.hws.edu/eck/cs124/javanotes9-swing/c3/ex3-ans.html
 *Date: 19/02/2025
 *Version: 1.0*/


import java.util.Scanner;

public class SimpleCalculator {

   public static void main(String[] args) {
    Scanner stdin = new Scanner(System.in);
      double firstNum;    // First number in the expression.
      double secondNum;   // Second number in the expression.
      char operator;      // The operator in the expression.
      double value;       // The value of the expression.
      
      System.out.println("Enter expressions such as  2 + 2  or  34.2 * 7.81");
      System.out.println("using any of the operators +, -, *, /.");
      System.out.println("To end, enter a 0.");
      System.out.println();
      
      while (true) {
          
          /* Get user's input, ending program if first number is 0. */
      
          System.out.print("? ");
          firstNum = stdin.nextDouble();
          if (firstNum == 0)
             break;
          operator = stdin.next().charAt(0);
          secondNum = stdin.nextDouble();
          
          /* Compute the value of the expression. */
          
          switch (operator) {
              case '+' -> value = firstNum + secondNum;
              case '-' -> value = firstNum - secondNum;
              case '*' -> value = firstNum * secondNum;
              case '/' -> value = firstNum / secondNum;
              default -> {
                 System.out.println("Unknown operator: " + operator);
                 continue;  // Back to start of loop!
              }
          } // end switch
          
          /* Display the value. */
          
          System.out.println("Value is " + value);
          System.out.println();
                    
      } // end while
      
      System.out.println("Good bye");
        stdin.close();
   }  // end main()

}  // end class SimpleCalculator