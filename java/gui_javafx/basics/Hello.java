/**
 * 
 * Basic JavaFX application
 * 
 * File: App.java
 * Author: Anthony Bañon
 * Created: 2025-06-15
 * Last Updated: 2025-06-15
 */


package gui_javafx.basics;

import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Label;
import javafx.stage.Stage;

public class Hello extends Application {
    @Override
    public void start(Stage stage) {
        Label label = new Label("¡Hola, JavaFX!");
        Scene scene = new Scene(label, 300, 200);
        stage.setScene(scene);
        stage.setTitle("Prueba JavaFX");
        stage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
