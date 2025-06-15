package gui_javafx.event_handling.student;
import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.layout.*;
import javafx.stage.Stage;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;

public class StudentManagementApp extends Application {
    
    // Variables globales para los controles de la interfaz
    private TextField studentNameField;
    private TextField studentIDField;
    private ListView<String> studentListView;
    private ComboBox<String> courseComboBox;
    private ComboBox<String> gradeComboBox;
    
    public static void main(String[] args) {
        launch(args);
    }

    @Override
    public void start(Stage primaryStage) {
        // Layout principal
        BorderPane root = new BorderPane();
        
        // Sección de entrada de datos de estudiante
        VBox inputBox = new VBox(10);
        Label nameLabel = new Label("Student Name:");
        studentNameField = new TextField();
        Label idLabel = new Label("Student ID:");
        studentIDField = new TextField();
        Button addButton = new Button("Add Student");
        
        inputBox.getChildren().addAll(nameLabel, studentNameField, idLabel, studentIDField, addButton);
        
        // Sección de lista de estudiantes
        studentListView = new ListView<>();
        Button updateButton = new Button("Update Student");
        Button viewButton = new Button("View Student Details");
        
        VBox studentBox = new VBox(10);
        studentBox.getChildren().addAll(updateButton, viewButton, studentListView);
        
        // Sección de inscripción a cursos
        courseComboBox = new ComboBox<>();
        courseComboBox.getItems().addAll("Math", "Science", "History");
        Button enrollButton = new Button("Enroll in Course");
        
        VBox enrollmentBox = new VBox(10);
        enrollmentBox.getChildren().addAll(courseComboBox, enrollButton);
        
        // Sección de gestión de calificaciones
        gradeComboBox = new ComboBox<>();
        gradeComboBox.getItems().addAll("A", "B", "C", "D", "F");
        Button assignGradeButton = new Button("Assign Grade");
        
        VBox gradeBox = new VBox(10);
        gradeBox.getChildren().addAll(gradeComboBox, assignGradeButton);
        
        // Evento de agregar estudiante
        addButton.setOnAction(new EventHandler<ActionEvent>() {
            @Override
            public void handle(ActionEvent event) {
                String studentName = studentNameField.getText();
                String studentID = studentIDField.getText();
                // Agregar estudiante a la lista
                studentListView.getItems().add(studentName + " - " + studentID);
            }
        });
        
        // Evento de actualizar estudiante
        updateButton.setOnAction(new EventHandler<ActionEvent>() {
            @Override
            public void handle(ActionEvent event) {
                // Lógica para actualizar información del estudiante
            }
        });
        
        // Evento de inscripción en curso
        enrollButton.setOnAction(new EventHandler<ActionEvent>() {
            @Override
            public void handle(ActionEvent event) {
                //String selectedCourse = courseComboBox.getValue();
                // Lógica para inscribir al estudiante en el curso seleccionado
            }
        });
        
        // Evento de asignación de calificación
        assignGradeButton.setOnAction(new EventHandler<ActionEvent>() {
            @Override
            public void handle(ActionEvent event) {
                //String selectedGrade = gradeComboBox.getValue();
                // Lógica para asignar calificación al estudiante
            }
        });
        
        // Organizar los componentes en la interfaz
        root.setTop(inputBox);
        root.setLeft(studentBox);
        root.setCenter(enrollmentBox);
        root.setRight(gradeBox);
        
        Scene scene = new Scene(root, 800, 600);
        primaryStage.setTitle("Student Management System");
        primaryStage.setScene(scene);
        primaryStage.show();
    }
}
