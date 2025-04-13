/* Description: Main program to see anidations
 * File name: Main.java
 * Creation date: 17/03/2025 */


package introduction.chapter5.nested;


public class Main {
    public static void main(String[] args) {

        // Static nested class
        StaticNestedClass.Nested nested = new StaticNestedClass.Nested();
        nested.display();

        // Non-static nested class
        NonStaticNestedClass outer = new NonStaticNestedClass();  // Creating instance of outer class
        NonStaticNestedClass.Inner inner = outer.new Inner();  // Creating instance of inner class
        inner.display();
        
        // Local class inside a method
        WithinAMethod method = new WithinAMethod();  // Creating instance of outer class
        method.myMethod();  // Calling method of outer class
    }
}
  
