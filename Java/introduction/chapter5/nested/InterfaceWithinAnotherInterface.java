/* Description: This program demonstrates the use of interface within another interface.
 * File name: InterfaceWithinAnotherInterface.java
 * Creation date: 17/03/2025
 * Last update: 17/03/2025*/

package Java.introduction.chapter5.nested;

// Interface within another interface
interface OuterInterface {  
    interface InnerInterface {  // Static and public by default
        void show();
    }
}

// Implementing class
class ImplementingClass implements OuterInterface.InnerInterface {  // Implementing inner interface
    public void show() {
        System.out.println("Inside nested interface");
    }
}

public class InterfaceWithinAnotherInterface {
    public static void main(String[] args) {

        // Creating instance of inner interface
        OuterInterface.InnerInterface obj = new ImplementingClass();
        obj.show();
    }
}
