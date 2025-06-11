package projects.small_projects.student_manager.src.methods.read_register;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.Properties;
import java.io.FileInputStream;
import java.io.IOException;
import java.util.Scanner;
import projects.small_projects.student_manager.src.database.DatabaseConnection;

public class ReadEntity extends DatabaseConnection{
    public String dbUrl;
    public ReadEntity() {
        // Cargar propiedades
        Properties properties = new Properties();
        try (FileInputStream input = new FileInputStream("src/database/DBconfiguration.properties")) {
            properties.load(input);
            dbUrl = properties.getProperty("db.url");
        } catch (IOException e) {
            System.out.println("Error al cargar las propiedades de la base de datos: " + e.getMessage());
        }
    }

    public void readStudent() {
        if (!checkRecords("alumno")) { // Verificar si hay registros de alumnos
            return; // Regresar al menú sin hacer nada más
        }
        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingrese el DNI del alumno para buscar: ");
        int dni = scanner.nextInt();

        // Estableciendo conexión a DB y ejecutar la consulta
        try (Connection connection = DriverManager.getConnection(dbUrl)) {
            String sql = "SELECT * FROM alumno WHERE id_alumnoDNI = ?";
            PreparedStatement preparedStatement = connection.prepareStatement(sql);
            preparedStatement.setInt(1, dni);

            ResultSet resultSet = preparedStatement.executeQuery();
            if (resultSet.next()) {
                System.out.println("Alumno encontrado:");
                System.out.println("DNI: " + resultSet.getInt("id_alumnoDNI"));
                System.out.println("Nombre: " + resultSet.getString("nombre_alumno"));
                System.out.println("Apellido: " + resultSet.getString("apellido_alumno"));
                System.out.println("Fecha de Nacimiento: " + resultSet.getString("fecha_nacimiento"));
                System.out.println("Dirección: " + resultSet.getString("direccion"));
            } else {
                System.out.println("No se encontró el alumno con DNI: " + dni);
            }
        } catch (SQLException e) {
            System.out.println("Error inesperado al intentar conectar a la base de datos: " + e.getMessage());
        }
    scanner.close();
    }

    public void readTeacher() {
        if (!checkRecords("profesor")) { // Verificar si hay registros de alumnos
            return; // Regresar al menú sin hacer nada más
        }
        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingrese el DNI del profesor para buscar: ");
        int id = scanner.nextInt();

        // Estableciendo conexión a DB y ejecutar la consulta
        try (Connection connection = DriverManager.getConnection(dbUrl)) {
            String sql = "SELECT * FROM profesor WHERE id_profesorDNI = ?";
            PreparedStatement preparedStatement = connection.prepareStatement(sql);
            preparedStatement.setInt(1, id);

            ResultSet resultSet = preparedStatement.executeQuery();
            if (resultSet.next()) {
                System.out.println("Profesor encontrado:");
                System.out.println("DNI: " + resultSet.getInt("id_profesor"));
                System.out.println("Nombre: " + resultSet.getString("nombre_profesor"));
                System.out.println("Apellido: " + resultSet.getString("apellido_profesor"));
            } else {
                System.out.println("No se encontró el profesor con DNI: " + id);
            }
        } catch (SQLException e) {
            System.out.println("Error inesperado al intentar conectar a la base de datos: " + e.getMessage());
        }
        scanner.close();
    }

    public void readSubject() {
        if (!checkRecords("materia")) { // Verificar si hay registros de alumnos
            return; // Regresar al menú sin hacer nada más
        }
        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingrese el Nombre de la materia para buscar: ");
        int id = scanner.nextInt();

        // Estableciendo conexión a DB y ejecutar la consulta
        try (Connection connection = DriverManager.getConnection(dbUrl)) {
            String sql = "SELECT * FROM materia WHERE id_materia = ?";
            PreparedStatement preparedStatement = connection.prepareStatement(sql);
            preparedStatement.setInt(1, id);

            ResultSet resultSet = preparedStatement.executeQuery();
            if (resultSet.next()) {
                System.out.println("Materia encontrada:");
                System.out.println("ID: " + resultSet.getInt("id_materia"));
                System.out.println("Nombre: " + resultSet.getString("nombre_materia"));
            } else {
                System.out.println("No se encontró la materia con ID: " + id);
            }
        } catch (SQLException e) {
            System.out.println("Error inesperado al intentar conectar a la base de datos: " + e.getMessage());
        }
        scanner.close();
    }
}