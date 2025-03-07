import java.util.HashMap;
import java.util.Map;

public class Student {
    private String name;  // Student's name
    private int id;  // Unique ID to identify the student
    private Map<Course, Double> grades;  // Map to store courses and grades for the student

    // Constructor to initialize the student with name, ID, and an empty grades map
    public Student(String name, int id) {
        this.name = name;
        this.id = id;
        this.grades = new HashMap<>();
    }

    // Getter and setter methods for the attributes
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getId() {
        return id;
    }

    // Method to enroll a student in a course
    public void enrollInCourse(Course course) throws IllegalArgumentException {
        if (course.getCurrentEnrollment() >= course.getCapacity()) { // Check if the course is full
            throw new IllegalArgumentException("The course is full. Cannot enroll.");
        }
        course.enrollStudent();  // Increase the current enrollment in the course
        grades.put(course, null); // Add the course to the student's course list with an initial null grade
    }

    // Method to assign a grade to a student in a specific course
    public void assignGrade(Course course, double grade) throws IllegalArgumentException {
        if (grade < 0 || grade > 100) { // Validate the grade range
            throw new IllegalArgumentException("Invalid grade. It must be between 0 and 100.");
        }
        if (!grades.containsKey(course)) { // Check if the student is enrolled in the course
            throw new IllegalArgumentException("The student is not enrolled in this course.");
        }
        grades.put(course, grade);  // Assign the grade to the corresponding course
    }

    // Method to calculate the overall grade for the student across all courses
    public double calculateOverallGrade() {
        double total = 0;
        int count = 0;
        for (Double grade : grades.values()) {
            if (grade != null) { // Only count non-null grades
                total += grade;
                count++;
            }
        }
        return count > 0 ? total / count : 0;  // Return the average, or 0 if no grades are assigned
    }
}
