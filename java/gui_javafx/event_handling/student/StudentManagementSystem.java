package gui_javafx.event_handling.student;    
import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.layout.*;
import javafx.stage.Stage;
import javafx.event.*;

public class StudentManagementSystem extends Application {

    // Variables to store student and course information
    private ListView<String> studentList = new ListView<>();
    private ComboBox<String> courseDropdown = new ComboBox<>();
    private TextField studentNameField = new TextField();
    private TextField studentIDField = new TextField();
    private TextArea outputArea = new TextArea();

    @Override
    public void start(Stage primaryStage) {
        // Create the main layout
        VBox root = new VBox(10);

        // GUI Components: Labels, Buttons, and Text Fields
        Label studentLabel = new Label("Student Name:");
        Label studentIDLabel = new Label("Student ID:");
        Button addStudentButton = new Button("Add Student");
        Button updateStudentButton = new Button("Update Student");
        Button viewStudentButton = new Button("View Students");
        Button enrollButton = new Button("Enroll in Course");
        Button assignGradeButton = new Button("Assign Grade");

        // Add event handlers to buttons
        addStudentButton.setOnAction(new EventHandler<ActionEvent>() {
            @Override
            public void handle(ActionEvent event) {
                addStudent(); // Call method to add student
            }
        });

        updateStudentButton.setOnAction(new EventHandler<ActionEvent>() {
            @Override
            public void handle(ActionEvent event) {
                updateStudent(); // Call method to update student
            }
        });

        viewStudentButton.setOnAction(new EventHandler<ActionEvent>() {
            @Override
            public void handle(ActionEvent event) {
                viewStudents(); // Call method to view students
            }
        });

        enrollButton.setOnAction(new EventHandler<ActionEvent>() {
            @Override
            public void handle(ActionEvent event) {
                enrollInCourse(); // Call method to enroll student in course
            }
        });

        assignGradeButton.setOnAction(new EventHandler<ActionEvent>() {
            @Override
            public void handle(ActionEvent event) {
                assignGrade(); // Call method to assign grade to student
            }
        });

        // Add all components to the main layout
        root.getChildren().addAll(studentLabel, studentNameField, studentIDLabel, studentIDField, addStudentButton, 
                                  updateStudentButton, viewStudentButton, studentList, enrollButton, courseDropdown,
                                  assignGradeButton, outputArea);

        // Set up the scene with the main layout and show the application
        Scene scene = new Scene(root, 400, 400);
        primaryStage.setTitle("Student Management System");
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    // Function to add a new student to the system
    private void addStudent() {
        String studentName = studentNameField.getText(); // Get student name from input field
        String studentID = studentIDField.getText(); // Get student ID from input field
        if (!studentName.isEmpty() && !studentID.isEmpty()) { // Check if both fields are filled
            studentList.getItems().add(studentName + " (" + studentID + ")"); // Add student to the list
            outputArea.setText("Student added: " + studentName); // Show confirmation in output area
        } else {
            outputArea.setText("Please enter valid student information."); // Show error message if fields are empty
        }
    }

    // Function to update a student's information
    private void updateStudent() {
        if (!studentList.getSelectionModel().isEmpty()) { // Check if a student is selected
            //String selectedStudent = studentList.getSelectionModel().getSelectedItem(); // Get selected student
            String updatedInfo = studentNameField.getText() + " (" + studentIDField.getText() + ")"; // Update student info
            studentList.getItems().set(studentList.getSelectionModel().getSelectedIndex(), updatedInfo); // Update the list
            outputArea.setText("Student updated: " + updatedInfo); // Show confirmation in output area
        } else {
            outputArea.setText("Please select a student to update."); // Show error message if no student is selected
        }
    }

    // Function to view all registered students
    private void viewStudents() {
        outputArea.setText("Registered Students:\n"); // Show header for student list
        for (String student : studentList.getItems()) { // Loop through all students in the list
            outputArea.appendText(student + "\n"); // Append student names to the output area
        }
    }

    // Function to enroll a student in a course
    private void enrollInCourse() {
        String selectedCourse = courseDropdown.getValue(); // Get selected course
        if (selectedCourse != null && !studentList.getSelectionModel().isEmpty()) { // Check if course and student are selected
            outputArea.setText("Student enrolled in: " + selectedCourse); // Show confirmation in output area
        } else {
            outputArea.setText("Please select a student and a course."); // Show error message if no selection is made
        }
    }

    // Function to assign a grade to a student
    private void assignGrade() {
        String selectedStudent = studentList.getSelectionModel().getSelectedItem(); // Get selected student
        String grade = "A"; // Default grade (this would normally be an input in a real-world scenario)
        if (selectedStudent != null) { // Check if a student is selected
            outputArea.setText("Assigned grade " + grade + " to " + selectedStudent); // Show confirmation in output area
        } else {
            outputArea.setText("Please select a student."); // Show error message if no student is selected
        }
    }

    public static void main(String[] args) {
        launch(args); // Launch the JavaFX application
    }
}
