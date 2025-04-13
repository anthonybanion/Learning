package projects.studentManager.src.methods.createRegister;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.util.Scanner;
import java.util.Properties;
import java.io.FileInputStream;
import java.io.IOException;

public class CreateEntity {
    private String dbUrl;

    public CreateEntity() {
        // Cargar propiedades
        Properties properties = new Properties();
        try (FileInputStream input = new FileInputStream("src/database/DBconfiguration.properties")) {
            properties.load(input);
            dbUrl = properties.getProperty("db.url");
        } catch (IOException e) {
            System.out.println("Error al cargar las propiedades de la base de datos: " + e.getMessage());
        }
    }

    public void createStudent() {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingresa el DNI del alumno sin espacios ni puntos: ");
        int dni = scanner.nextInt();
        scanner.nextLine(); // Limpiar el buffer

        System.out.print("Ingrese el nombre del alumno: ");
        String nombre = scanner.nextLine();

        System.out.print("Ingrese el apellido del alumno: ");
        String apellido = scanner.nextLine();

        System.out.print("Ingrese la fecha de nacimiento del alumno (Formato esperado: DD-MM-AAAA): ");
        String fechaNacimiento = scanner.nextLine();

        System.out.print("Ingrese la dirección del alumno: ");
        String direccion = scanner.nextLine();

        // Estableciendo conexión a DB y ejecutar la inserción de los datos
        try (Connection connection = DriverManager.getConnection(dbUrl)) {
            String sql = "INSERT INTO alumno(id_alumnoDNI, nombre_alumno, apellido_alumno, fecha_nacimiento, direccion) VALUES (?, ?, ?, ?, ?)";
            PreparedStatement preparedStatement = connection.prepareStatement(sql);
            preparedStatement.setInt(1, dni);
            preparedStatement.setString(2, nombre);
            preparedStatement.setString(3, apellido);
            preparedStatement.setString(4, fechaNacimiento);
            preparedStatement.setString(5, direccion);

            int rowsAffected = preparedStatement.executeUpdate();
            if (rowsAffected > 0) {
                System.out.println("El registro del alumno fue creado exitosamente.");
            } else {
                System.out.println("Error inesperado al intentar crear el registro. Intente nuevamente.");
            }
        } catch (SQLException e) {
            System.out.println("Error inesperado al intentar conectar a la base de datos: " + e.getMessage());
        }
    scanner.close();
    }

    // Métodos para crear profesor y materia
    public void createProfessor() {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingrese el ID del profesor: ");
        int id = scanner.nextInt();
        scanner.nextLine(); // Limpiar el buffer

        System.out.print("Ingrese el nombre del profesor: ");
        String nombre = scanner.nextLine();

        System.out.print("Ingrese el apellido del profesor: ");
        String apellido = scanner.nextLine();

        // Estableciendo conexión a DB y ejecutar la inserción de los datos
        try (Connection connection = DriverManager.getConnection(dbUrl)) {
            String sql = "INSERT INTO profesor(id_profesorDNI, nombre_profesor, apellido_profesor) VALUES (?, ?, ?)";
            PreparedStatement preparedStatement = connection.prepareStatement(sql);
            preparedStatement.setInt(1, id);
            preparedStatement.setString(2, nombre);
            preparedStatement.setString(3, apellido);

            int rowsAffected = preparedStatement.executeUpdate();
            if (rowsAffected > 0) {
                System.out.println("El registro del profesor fue creado exitosamente.");
            } else {
                System.out.println("Error inesperado al intentar crear el registro. Intente nuevamente.");
            }
        } catch (SQLException e) {
            System.out.println("Error inesperado al intentar conectar a la base de datos: " + e.getMessage());
        }
    scanner.close();
    }

    public void createSubject() {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingrese el ID de la materia: ");
        int id = scanner.nextInt();
        scanner.nextLine(); // Limpiar el buffer

        System.out.print("Ingrese el nombre de la materia: ");
        String nombre = scanner.nextLine();

        // Estableciendo conexión a DB y ejecutar la inserción de los datos
        try (Connection connection = DriverManager.getConnection(dbUrl)) {
            String sql = "INSERT INTO materia(id_materia, nombre_materia) VALUES (?, ?)";
            PreparedStatement preparedStatement = connection.prepareStatement(sql);
            preparedStatement.setInt(1, id);
            preparedStatement.setString(2, nombre);

            int rowsAffected = preparedStatement.executeUpdate();
            if (rowsAffected > 0) {
                System.out.println("El registro de la materia fue creado exitosamente.");
            } else {
                System.out.println("Error inesperado al intentar crear el registro. Intente nuevamente.");
            }
        } catch (SQLException e) {
            System.out.println("Error inesperado al intentar conectar a la base de datos: " + e.getMessage());
        }
        scanner.close();
    }
}