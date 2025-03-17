/* Description: Static nested class in interface
 * File name: StatiClassesWithinInterfaces.java
 * Creation date: 17/03/2025*/

package Java.introduction.chapter5.nested;

interface OuterInterface {

    class StaticNestedClass {
        void show() {
            System.out.println("Inside static nested class in interface");
        }
    }
}

public class StatiClassesWithinInterfaces {
    public static void main(String[] args) {

        // Creating instance of static nested class
        OuterInterface.StaticNestedClass obj = new OuterInterface.StaticNestedClass();  
        obj.show();
    }
}