/*Brief: This program will convert a given number of eggs into
       the number of gross plus the number of dozens plus the
       number of left over eggs.
 *Detail: Exercise 2.5
 *Source: https://math.hws.edu/eck/cs124/javanotes9-swing/c2/ex5-ans.html
 *Date: 09/02/2025
 *Version: 1.0
*/


package introduction.chapter2;
import java.util.Scanner;  // Import the Scanner class
public class GrossAndDozens {

   public static void main(String[] args) {
        Scanner stdin = new Scanner(System.in);
   
      int eggs;         // Number of eggs, input by user.
      int gross;        // How many gross in that number of eggs?
      int aboveGross;   // How many eggs are left over, above an
                        //    integral number of gross?  This number
                        //    can be computed as eggs % 144, and is
                        //    in the range 0 to 143.  This number will
                        //    be divided into dozens and extras.
      int dozens;       // How many dozens in aboveGross?
      int extras;       // How many eggs are left over, above integral
                        //    numbers of gross and dozens? 
   
      System.out.print("How many eggs do you have?  ");
      eggs = stdin.nextInt();
      
      gross = eggs / 144;
      aboveGross = eggs % 144;
      
      dozens = aboveGross / 12;
      extras = aboveGross % 12;          
      
      System.out.print("Your number of eggs is ");
      System.out.print(gross);
      System.out.print(" gross, ");
      System.out.print(dozens);
      System.out.print(" dozen, and ");
      System.out.print(extras);
      System.out.println();
      stdin.close();
   }  // end main()

}  // end class