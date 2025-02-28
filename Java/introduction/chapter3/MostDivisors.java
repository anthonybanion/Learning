/*Brief: This program finds an integer between 1 and 10000 that has
 * the largest number of divisors.  It prints out the maximum
 * number of divisors and an integer that has that many divisors.
 *Detail: Exercise 3.2
 *Source: https://math.hws.edu/eck/cs124/javanotes9-swing/c3/ex2-ans.html
 *Date: 19/02/2025
 *Version: 1.0*/


 public class MostDivisors {

    public static void main(String[] args) {
    
        int N;            // One of the integers whose divisors we have to count.
        int maxDivisors;  // Maximum number of divisors seen so far.
        int numWithMax;   // A value of N that had the given number of divisors.
        
        maxDivisors = 1;  // Start with the fact that 1 has 1 divisor.
        numWithMax = 1;
 
        /* Process all the remaining values of N from 2 to 10000, and
           update the values of maxDivisors and numWithMax whenever we
           find a value of N that has more divisors than the current value
           of maxDivisors.
        */
        
        for ( N = 2;  N <= 10000;  N++ ) {
        
            int D;  // A number to be tested to see if it's a divisor of N.
            int divisorCount;  // Number of divisors of N.
            
            divisorCount = 0;
            
            for ( D = 1;  D <= N;  D++ ) {  // Count the divisors of N.
               if ( N % D == 0 )
                  divisorCount++;
            }
            
            if (divisorCount > maxDivisors) {
               maxDivisors = divisorCount;
               numWithMax = N;
            }
        
        }
        
        System.out.println("Among integers between 1 and 10000,");
        System.out.println("The maximum number of divisors is " + maxDivisors);
        System.out.println("A number with " + maxDivisors + " divisors is " + numWithMax);
    
    } // end main()
 
 }
 