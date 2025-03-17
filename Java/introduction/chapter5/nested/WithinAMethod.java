/* Description: Local class inside a method
 * File name: WithinAMethod.java
 * Creation date: 17/03/2025*/

package Java.introduction.chapter5.nested;

public class WithinAMethod {
    void myMethod() {
        
        class LocalClass {
            void display() {
                System.out.println("Inside local class");
            }
        }

        LocalClass local = new LocalClass();
        local.display();
    }
}
