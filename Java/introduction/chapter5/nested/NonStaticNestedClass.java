/* Description: Non-static nested class is a class which is declared inside another class but not as static.
 * File name:  NonStaticNestedClass.java
 * Creation date: 17/03/2025
 * Considerations: for a Non-static nested class,
                It can access all data members and methods of the outer class including private.
                It cannot have static data members and methods.
                It cannot access non-static data members and methods.
                It cannot access local variables of the method inside which it is defined.
                It is used to logically group classes that are only used in one place.
                It cannot exist without an instance of the outer class.
                It cannot be declared static.
                It can be declared private, public, protected, or default.
                It can extend any class and implement interfaces.
                It can be abstract or final.
                It can access the members of the outer class directly.
                It can be instantiated only within the outer class.
                It can be instantiated outside the outer class only through an object of the outer class.
                It can be declared as an anonymous class.
                It can be declared as a local class.
                It can be declared as a member class.
                It can be declared as a nested class.
                It can be declared as a top-level class.
                It can be declared as a static class.
                It can be declared as a static nested class.
                It can be declared as a non-static nested class.
                It can be declared as a nested interface.
                It can be declared as a nested enum.
                It can be declared as a nested annotation.
                It can be declared as a nested class.
                It can be declared as a nested interface.
                It can be declared as a nested enum.
                It can be declared as a nested annotation.
                It can be declared as a nested class.
                It can be declared as a nested interface.
                It can be declared as a nested enum.
                It can be declared as a nested annotation.
                It can be declared as a nested class.
                It can be declared as a nested interface.
                It can be declared as a nested enum.
                It can be declared as a nested annotation.
                It can be declared as a nested class.
                It can be declared as a nested interface.
                It can be declared as a nested enum.
                It can be declared as a nested annotation.
                It can be declared as a nested class.
                It can be declared as a nested interface.
                It can be declared as a nested enum.
                It can be declared as a nested annotation.
                It can be declared as a nested class.
                It can be declared as a nested interface
 */

 

package introduction.chapter5.nested;

class NonStaticNestedClass {
    class Inner {
        void display() {
            System.out.println("Inside inner class");
        }
    }
}

