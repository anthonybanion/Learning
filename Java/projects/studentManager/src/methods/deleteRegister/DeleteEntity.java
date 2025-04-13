package projects.studentManager.src.methods.deleteRegister;

import projects.studentManager.src.database.DatabaseConnection;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.util.Properties;
import java.io.FileInputStream;
import java.io.IOException;
import java.util.Scanner;

public class DeleteEntity extends DatabaseConnection {
    public String dbUrl;

    public DeleteEntity() {
        // Cargar propiedades
        Properties properties = new Properties();
        try (FileInputStream input = new FileInputStream("src/database/DBconfiguration.properties")) {
            properties.load(input);
            dbUrl = properties.getProperty("db.url");
        } catch (IOException e) {
            System.out.println("Error al cargar las propiedades de la base de datos: " + e.getMessage());
        }
    }

    public void deleteStudent() {
        if (!checkRecords("alumno")) { // Verificar si hay registros de alumnos
            return; // Regresar al menú sin hacer nada más
        }
        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingrese el DNI del alumno a eliminar: ");
        int dni = scanner.nextInt();

        // Estableciendo conexión a DB y ejecutar la eliminación
        try (Connection connection = DriverManager.getConnection(dbUrl)) {
            String sql = "DELETE FROM alumno WHERE id_alumnoDNI = ?";
            PreparedStatement preparedStatement = connection.prepareStatement(sql);
            preparedStatement.setInt(1, dni);

            int rowsAffected = preparedStatement.executeUpdate();
            if (rowsAffected > 0) {
                System.out.println("El registro del alumno fue eliminado exitosamente.");
            } else {
                System.out.println("No se encontró el alumno con DNI: " + dni);
            }
        } catch (SQLException e) {
            System.out.println("Error inesperado al intentar conectar a la base de datos: " + e.getMessage());
        }
        scanner.close();
    }

    public void deleteProfessor() {
        if (!checkRecords("profesor")) { // Verificar si hay registros de alumnos
            return; // Regresar al menú sin hacer nada más
        }
        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingrese el ID del profesor a eliminar: ");
        int id = scanner.nextInt();

        // Estableciendo conexión a DB y ejecutar la eliminación
        try (Connection connection = DriverManager.getConnection(dbUrl)) {
            String sql = "DELETE FROM profesor WHERE id_profesor = ?";
            PreparedStatement preparedStatement = connection.prepareStatement(sql);
            preparedStatement.setInt(1, id);

            int rowsAffected = preparedStatement.executeUpdate();
            if (rowsAffected > 0) {
                System.out.println("El registro del profesor fue eliminado exitosamente.");
            } else {
                System.out.println("No se encontró el profesor con ID: " + id);
            }
        } catch (SQLException e) {
            System.out.println("Error inesperado al intentar conectar a la base de datos: " + e.getMessage());
        }
        scanner.close();

    }

    public void deleteSubject() {
        if (!checkRecords("materia")) { // Verificar si hay registros de alumnos
            return; // Regresar al menú sin hacer nada más
        }
        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingrese el ID de la materia a eliminar: ");
        int id = scanner.nextInt();

        // Estableciendo conexión a DB y ejecutar la eliminación
        try (Connection connection = DriverManager.getConnection(dbUrl)) {
            String sql = "DELETE FROM materia WHERE id_materia = ?";
            PreparedStatement preparedStatement = connection.prepareStatement(sql);
            preparedStatement.setInt(1, id);

            int rowsAffected = preparedStatement.executeUpdate();
            if (rowsAffected > 0) {
                System.out.println("El registro de la materia fue eliminado exitosamente.");
            } else {
                System.out.println("No se encontró la materia con ID: " + id);
            }
        } catch (SQLException e) {
            System.out.println("Error inesperado al intentar conectar a la base de datos: " + e.getMessage());
        }
        scanner.close();
    }

    // public void deleteAll() {
    //     Scanner scanner = new Scanner(System.in);
    //     if (!hasRecords("alumno") &&
    //         !hasRecords("profesor") &&
    //         !hasRecords("materia")) {
    //         System.out.println("Error, no hay registros en ninguna de las tablas. Primero debe ingresar datos.");
    //         return; // Regresar al menú sin hacer nada más
    //     }
    //     int userDecisions;
    //     System.out.print("¡ATENCION! ESTA OPCION BORRA EL CONTENIDO DE LA BASE DE DATOS");

    //     while (true) {
    //         System.out.print("\n¿USTED ESTA SEGURO DE CONTINUAR?");
    //         System.out.print("""
    //                 \n
    //                 1. SI
    //                 2. NO
    //                 """);
    //         userDecisions = scanner.nextInt();

    //         // Este if solo se validará si el usuario ingresó la opción 1
    //         if (userDecisions == 1) {
    //             // Estableciendo conexión en la DB y ejecuta la eliminación completa
    //             try (Connection connection = DriverManager.getConnection(dbUrl)) {
    //                 // Ejecutar eliminación para cada tabla
    //                 String[] tables = {"alumno", "profesor", "materia", "alumno_materia"};
    //                 for (String table : tables) {
    //                     String sql = "DELETE FROM " + table;
    //                     try (PreparedStatement preparedStatement = connection.prepareStatement(sql)) {
    //                         int rowsAffected = preparedStatement.executeUpdate();
    //                         System.out.println("Se eliminaron " + rowsAffected + " registros de la tabla " + table + ".");
    //                     }
    //                 }
    //                 System.out.println("Todos los registros de la base de datos fueron eliminados exitosamente.");
    //             } catch (SQLException e) {
    //                 System.out.println("Error inesperado al intentar conectar a la base de datos: " + e.getMessage());
    //             }
    //             break; // Sale del bucle y regresa al menú principal
    //         } else if (userDecisions == 2) {
    //             System.out.println("No se efectuaron eliminaciones. Los registros permanecen sin cambios.");
    //             return; // Regresa al menú de eliminación
    //         } else {
    //             System.out.println("Opción no válida. Por favor, ingrese 1 o 2.");
    //         }
    //     }
    // }
    public void deleteAll() {
        Scanner scanner = new Scanner(System.in);
        try {
            if (!hasRecords("alumno") &&
                !hasRecords("profesor") &&
                !hasRecords("materia")) {
                System.out.println("Error, no hay registros en ninguna de las tablas. Primero debe ingresar datos.");
                return;
            }
            int userDecisions;
            System.out.print("¡ATENCION! ESTA OPCION BORRA EL CONTENIDO DE LA BASE DE DATOS");
    
            while (true) {
                System.out.print("\n¿USTED ESTA SEGURO DE CONTINUAR?");
                System.out.print("""
                        \n
                        1. SI
                        2. NO
                        """);
                userDecisions = scanner.nextInt();
    
                if (userDecisions == 1) {
                    try (Connection connection = DriverManager.getConnection(dbUrl)) {
                        String[] tables = {"alumno", "profesor", "materia", "alumno_materia"};
                        for (String table : tables) {
                            String sql = "DELETE FROM " + table;
                            try (PreparedStatement preparedStatement = connection.prepareStatement(sql)) {
                                int rowsAffected = preparedStatement.executeUpdate();
                                System.out.println("Se eliminaron " + rowsAffected + " registros de la tabla " + table + ".");
                            }
                        }
                        System.out.println("Todos los registros de la base de datos fueron eliminados exitosamente.");
                    } catch (SQLException e) {
                        System.out.println("Error inesperado al intentar conectar a la base de datos: " + e.getMessage());
                    }
                    break;
                } else if (userDecisions == 2) {
                    System.out.println("No se efectuaron eliminaciones. Los registros permanecen sin cambios.");
                    return;
                } else {
                    System.out.println("Opción no válida. Por favor, ingrese 1 o 2.");
                }
            }
        } finally {
            scanner.close(); // Cierra el Scanner para evitar la advertencia
        }
    }
    

}