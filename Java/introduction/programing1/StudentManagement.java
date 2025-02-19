import java.util.ArrayList;
import java.util.Scanner;

public class StudentManagement {
    // Static list stores registered students
    private static ArrayList<Student> students = new ArrayList<>();
    // Student counter, increases every time a student is added
    private static int totalStudents = 0;
    private static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        // Menu that continuously displays options for the administrator to select
        while (true) {
            System.out.println("\n--- Student Management System ---");
            System.out.println("1. Add new student");
            System.out.println("2. Update student information");
            System.out.println("3. View student details");
            System.out.println("4. Exit");
            System.out.print("Select an option: ");
            
            int choice = scanner.nextInt();
            scanner.nextLine(); // Consume the newline character after the number input

            switch (choice) {
                case 1:
                    addStudent(); // Call method to add a new student
                    break;
                case 2:
                    updateStudent(); // Call method to update student information
                    break;
                case 3:
                    viewStudent(); // Call method to view student details
                    break;
                case 4:
                    System.out.println("Exiting the system..."); // Exit the program
                    return;
                default:
                    System.out.println("Invalid option. Please try again."); // Handle invalid option
            }
        }
    }

    // Method to add a new student
    private static void addStudent() {
        System.out.print("Enter the student's name: ");
        String name = scanner.nextLine();
        System.out.print("Enter the student's age: ");
        int age = scanner.nextInt();
        scanner.nextLine(); // Consume the newline character after the number input
        System.out.print("Enter the student's grade: ");
        String grade = scanner.nextLine();

        // Create a new student and assign an ID
        int id = ++totalStudents;
        students.add(new Student(id, name, age, grade));  // Add the student to the list
        System.out.println("Student added successfully with ID: " + id);
    }

    // Method to update the information of an existing student
    private static void updateStudent() {
        System.out.print("Enter the student ID to update: ");
        int id = scanner.nextInt();
        scanner.nextLine(); // Consume the newline character after the number input

        // Search for the student with the entered ID
        for (Student student : students) {
            if (student.getId() == id) {  
                // Update student details
                System.out.print("Enter the new name: ");
                student.setName(scanner.nextLine());
                System.out.print("Enter the new age: ");
                student.setAge(scanner.nextInt());
                scanner.nextLine(); // Consume the newline character after the number input
                System.out.print("Enter the new grade: ");
                student.setGrade(scanner.nextLine());
                System.out.println("Information updated successfully.");
                return;
            }
        }
        System.out.println("Student with ID " + id + " not found.");
    }

    // Method to view the details of a specific student
    private static void viewStudent() {
        System.out.print("Enter the student ID to view: ");
        int id = scanner.nextInt();
        scanner.nextLine(); // Consume the newline character after the number input

        // Search for the student with the entered ID and display the details
        for (Student student : students) {
            if (student.getId() == id) {
                System.out.println("\nStudent Details:");
                System.out.println(student); // Print the student object using toString()
                return;
            }
        }
        System.out.println("Student with ID " + id + " not found.");
    }
}

class Student {
    private int id;
    private String name;
    private int age;
    private String grade;

    // Constructor to initialize a student with their details
    public Student(int id, String name, int age, String grade) {
        this.id = id;
        this.name = name;
        this.age = age;
        this.grade = grade;
    }

    // Getters and setters for student details
    public int getId() { return id; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public int getAge() { return age; }
    public void setAge(int age) { this.age = age; }
    public String getGrade() { return grade; }
    public void setGrade(String grade) { this.grade = grade; }

    // Override toString method to print student details in a readable format
    @Override
    public String toString() {
        return "ID: " + id + "\nName: " + name + "\nAge: " + age + "\nGrade: " + grade;
    }
}
