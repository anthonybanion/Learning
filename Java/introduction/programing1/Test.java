
public class Test {
    static class Example {
        static int counter = 0; // Static variable shared by all instances
        int value; // Instance variable
        
        public Example(int value) {
            this.value = value;
            counter++; // Increments with each new instance created
        }
        
        static void showCounter() {
            System.out.println("Instances created: " + counter);
        }
        
        void showValue() {
            System.out.println("Instance value: " + value);
        }
    }

    public static void main(String[] args) {
        Example e1 = new Example(10);
        Example e2 = new Example(20);
        
        e1.showValue(); // Instance value: 10
        e2.showValue(); // Instance value: 20
        
        Example.showCounter(); // Instances created: 2
    }
}