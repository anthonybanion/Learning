/* Description: Static nested class is a class which is declared as static. 
 * File name: StaticNestedClass.java
 * Creation date: 17/03/2025
 * Considerations: for a Static nested class,
                It cannot access non-static data members and methods. 
                It can access static data members of outer class including private. 
                It is used to group classes that belong together. 
                It can access static data members of outer class including private. 
                It cannot access non-static data members and methods.*/


package introduction.chapter5.nested;

public class StaticNestedClass {
    public static class Nested {
        void display() {
            System.out.println("Inside static nested class");
        }
    }
}
