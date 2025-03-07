public class Course {
    private String code;  // Unique code to identify the course
    private String name;  // Name of the course
    private int capacity;  // Maximum capacity of the course
    private int currentEnrollment;  // Number of students currently enrolled in the course

    // Constructor to initialize the course with a code, name, and capacity
    public Course(String code, String name, int capacity) {
        this.code = code;
        this.name = name;
        this.capacity = capacity;
        this.currentEnrollment = 0; // Initially, there are no students enrolled
    }

    // Getter methods to retrieve course information
    public String getCode() {
        return code;
    }

    public String getName() {
        return name;
    }

    public int getCapacity() {
        return capacity;
    }

    public void setCapacity(int newCapacity) {
        this.capacity = newCapacity;
    }

    public int getCurrentEnrollment() {
        return currentEnrollment;
    }

    // Method to enroll a student in the course
    public void enrollStudent() {
        if (currentEnrollment < capacity) {  // Check if there is space available in the course
            currentEnrollment++;
        }
    }

    // Method to update the capacity of the course
    public void updateCapacity(int newCapacity) {
        this.capacity = newCapacity;
    }
}
