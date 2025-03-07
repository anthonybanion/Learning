import java.util.Scanner;

public class AdministratorInterface {
    private static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        boolean running = true;

        while (running) {
            // options menu
            System.out.println("Welcome to the Course and Grade Management System.");
            System.out.println("1. Add Course");
            System.out.println("2. Enroll Student");
            System.out.println("3. Assign Grade");
            System.out.println("4. Calculate Overall Grade");
            System.out.println("5. Update Course Capacity");
            System.out.println("6. Update Student Name");
            System.out.println("7. Exit");

            int choice = scanner.nextInt();
            scanner.nextLine(); // Clean the buffer

            switch (choice) {
                case 1:
                    addCourse();
                    break;
                case 2:
                    enrollStudent();
                    break;
                case 3:
                    assignGrade();
                    break;
                case 4:
                    calculateOverallGrade();
                    break;
                case 5:
                    updateCourseCapacity();
                    break;
                case 6:
                    updateStudentName();
                    break;
                case 7:
                    running = false;
                    System.out.println("Exiting...");
                    break;
                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        }
    }

    private static void addCourse() {
       // request data to create a new course
        System.out.print("Enter course code: ");
        String code = scanner.nextLine();
        System.out.print("Enter course name: ");
        String name = scanner.nextLine();
        System.out.print("Enter course maximum capacity: ");
        int capacity = scanner.nextInt();
        scanner.nextLine();

        CourseManagement.addCourse(code, name, capacity);
        System.out.println("Course added successfully.");
    }

    private static void enrollStudent() {
       // request data to register a student
        System.out.print("Enter student ID: ");
        int studentId = scanner.nextInt();
        scanner.nextLine(); 
        System.out.print("Enter student name: ");
        String studentName = scanner.nextLine();
        Student student = new Student(studentName, studentId);

        System.out.print("Enter course code to enroll in: ");
        String courseCode = scanner.nextLine();
        Course course = getCourseByCode(courseCode);

        if (course != null) {
            CourseManagement.enrollStudent(student, course);
            System.out.println("Student enrolled successfully.");
        } else {
            System.out.println("Course not found.");
        }
    }

    private static void assignGrade() {
        // Request data to assign a qualification
        System.out.print("Enter student ID: ");
        int studentId = scanner.nextInt();
        scanner.nextLine(); 
        System.out.print("Enter course code: ");
        String courseCode = scanner.nextLine();
        System.out.print("Enter grade: ");
        double grade = scanner.nextDouble();
        scanner.nextLine(); 

        Student student = CourseManagement.getStudentById(studentId);
        Course course = getCourseByCode(courseCode);

        if (course != null) {
            CourseManagement.assignGrade(student, course, grade);
            System.out.println("Grade assigned successfully.");
        } else {
            System.out.println("Course not found.");
        }
    }

    private static void calculateOverallGrade() {
        // Request data to calculate the total rating
        System.out.print("Enter student ID: ");
        int studentId = scanner.nextInt();
        Student student = new Student("Unknown", studentId);

        double overallGrade = CourseManagement.calculateOverallGrade(student);
        System.out.println("Overall grade for student " + studentId + ": " + overallGrade);
    }

    private static void updateCourseCapacity() {
        // Request data to update the course capacity
        System.out.print("Enter course code to update: ");
        String courseCode = scanner.nextLine();
        Course course = getCourseByCode(courseCode);

        if (course != null) {
            System.out.print("Enter new capacity: ");
            int newCapacity = scanner.nextInt();
            scanner.nextLine(); 
            course.setCapacity(newCapacity);
            System.out.println("Course capacity updated.");
        } else {
            System.out.println("Course not found.");
        }
    }

    private static void updateStudentName() {
        // Request data to update the student's name
        System.out.print("Enter student ID to update: ");
        int studentId = scanner.nextInt();
        scanner.nextLine();
        System.out.print("Enter new student name: ");
        String newName = scanner.nextLine();
        CourseManagement.updateStudentName(studentId, newName);
        System.out.println("Student name updated.");
    }

    private static Course getCourseByCode(String code) {
        // logic to search for the course by code
        return CourseManagement.getCourses().stream()
                .filter(course -> course.getCode().equals(code))
                .findFirst()
                .orElse(null);
    }
}
