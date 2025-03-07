import java.util.ArrayList;
import java.util.List;

public class CourseManagement {
    private static List<Course> courses = new ArrayList<>(); // List of all courses
    private static List<Student> students = new ArrayList<>(); // List of all students

    // Static method to add a new course
    public static void addCourse(String code, String name, int capacity) {
        courses.add(new Course(code, name, capacity));
    }

    // Static method to enroll a student in a course
    public static void enrollStudent(Student student, Course course) {
        try {
            student.enrollInCourse(course);
        } catch (IllegalArgumentException e) {
            System.out.println(e.getMessage());  // Handle the error if the course is full
        }
    }

    // Static method to assign a grade to a student in a course
    public static void assignGrade(Student student, Course course, double grade) {
        try {
            student.assignGrade(course, grade);
        } catch (IllegalArgumentException e) {
            System.out.println(e.getMessage());  // Handle the error if the student is not enrolled in the course
        }
    }

    // Static method to calculate the overall grade for a student
    public static double calculateOverallGrade(Student student) {
        return student.calculateOverallGrade();
    }

    // Methods to add students to the global list
    public static void addStudent(String name, int id) {
        students.add(new Student(name, id));
    }

    // Methods to retrieve the lists of courses and students
    public static List<Course> getCourses() {
        return courses;
    }

    public static List<Student> getStudents() {
        return students;
    }

    // Static method to update the name of a student
    public static void updateStudentName(int studentId, String newName){
        for (Student student : students) {
            if (student.getId() == studentId) {
                student.setName(newName);
                System.out.println("Student name updated.");
                return;
            }
        }
        System.out.println("Student not found.");
    }

    // Static method to retrieve a student by ID
    public static Student getStudentById(int studentId) {
        for (Student student : students) {
            if (student.getId() == studentId) {
                return student;
            }
        }
        return null; // Return null if student is not found
    }
}
