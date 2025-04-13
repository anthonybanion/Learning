/*Brief: This program simulates rolling a pair of dice.
        The number that comes up on each die is output,
        followed by the total of the two dice.
 *Detail: Exercise 2.2
 *Source: https://math.hws.edu/eck/cs124/javanotes9-swing/c2/ex2-ans.html
 *Date: 09/02/2025
 *Version: 1.0
*/
package introduction.chapter2;
public class RollTheDice {
 
    public static void main(String[] args) {
    
        int die1;   // The number on the first die.
        int die2;   // The number on the second die.
        int roll;   // The total roll (sum of the two dice).
        
        die1 = (int)(Math.random()*6) + 1;
        die2 = (int)(Math.random()*6) + 1;
        roll = die1 + die2;
        
        System.out.println("The first die comes up " + die1);
        System.out.println("The second die comes up " + die2);
        System.out.println("Your total roll is " + roll);

    }  // end main()
 
}  // end class