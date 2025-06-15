/*Description: 
 * File name: 
 * Creation date: 18/03/2025
 */

package gui_javafx.event_handling.student;

import javafx.application.Application;
import javafx.scene.Scene;
import javafx.stage.Stage;
import javafx.scene.control.*;
import javafx.scene.layout.*;
import javafx.collections.*;
import javafx.geometry.Pos;
import javafx.beans.property.*;

public class StudentCRUD extends Application {
    
    private TableView<Student> table;
    private ObservableList<Student> students;
    
    public void start(Stage stage) {
        students = FXCollections.observableArrayList();
        
        // Botones principales
        Button btnCreate = new Button("Create Student");
        Button btnShow = new Button("Show Students");
        
        btnCreate.setOnAction(e -> showCreateScreen(stage));
        btnShow.setOnAction(e -> showStudentList(stage));
        
        HBox menu = new HBox(20, btnCreate, btnShow);
        menu.setAlignment(Pos.CENTER);
        
        Scene mainScene = new Scene(menu, 400, 200);
        stage.setScene(mainScene);
        stage.setTitle("Student Management");
        stage.show();
    }
    
    private void showCreateScreen(Stage stage) {
        VBox layout = new VBox(10);
        layout.setAlignment(Pos.CENTER);
        
        TextField nameField = new TextField();
        nameField.setPromptText("Name");
        TextField surnameField = new TextField();
        surnameField.setPromptText("Surname");
        TextField dniField = new TextField();
        dniField.setPromptText("DNI");
        
        Button saveButton = new Button("Save Student");
        saveButton.setOnAction(e -> {
            students.add(new Student(nameField.getText(), surnameField.getText(), dniField.getText()));
            showStudentList(stage);
        });
        
        layout.getChildren().addAll(nameField, surnameField, dniField, saveButton);
        
        Scene scene = new Scene(layout, 400, 300);
        stage.setScene(scene);
    }
    
    private void showStudentList(Stage stage) {
        table = new TableView<>(students);
        
        TableColumn<Student, String> nameCol = new TableColumn<>("Name");
        nameCol.setCellValueFactory(data -> data.getValue().nameProperty());
        
        TableColumn<Student, String> surnameCol = new TableColumn<>("Surname");
        surnameCol.setCellValueFactory(data -> data.getValue().surnameProperty());
        
        TableColumn<Student, String> dniCol = new TableColumn<>("DNI");
        dniCol.setCellValueFactory(data -> data.getValue().dniProperty());
        
        //table.getColumns().addAll(nameCol, surnameCol, dniCol);
        
        Button backButton = new Button("Back");
        backButton.setOnAction(e -> start(stage));
        
        VBox layout = new VBox(10, table, backButton);
        layout.setAlignment(Pos.CENTER);
        
        Scene scene = new Scene(layout, 500, 400);
        stage.setScene(scene);
    }
    
    public static void main(String[] args) {
        launch();
    }
}

class Student {
    private StringProperty name, surname, dni;
    
    public Student(String name, String surname, String dni) {
        this.name = new SimpleStringProperty(name);
        this.surname = new SimpleStringProperty(surname);
        this.dni = new SimpleStringProperty(dni);
    }
    
    public StringProperty nameProperty() { return name; }
    public StringProperty surnameProperty() { return surname; }
    public StringProperty dniProperty() { return dni; }
}
