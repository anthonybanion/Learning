package projects.studentManager.src.database;

import java.io.FileInputStream;
import java.io.IOException;
import java.sql.*;
import java.util.Properties;

public class DatabaseConnection {
    private Connection connection;
    public String dbUrl;

    public DatabaseConnection() {
        // Cargar propiedades
        Properties properties = new Properties();
        try (FileInputStream input = new FileInputStream("projects/studentManager/src/database/DBconfiguration.properties")) {
            properties.load(input);
        } catch (IOException e) {
            e.printStackTrace();
            System.out.println();
        }

        // Obtener la URL de la base de datos
            // Corregir la asignación a la variable de instancia
        this.dbUrl = properties.getProperty("db.url");
        //String dbUrl = properties.getProperty("db.url");

        try {
            Class.forName("org.sqlite.JDBC");
        } catch (ClassNotFoundException e) {
            System.out.println("Error: No se encontró el driver de SQLite");
        }


        // Establecer conexión
        try {
            connection = DriverManager.getConnection(dbUrl);
            System.out.println("Conexión a la base de datos establecida.");
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    // Método para verificar si hay registros en una tabla
    public boolean hasRecords(String tableName) {
        try (Connection connection = DriverManager.getConnection(dbUrl)) {
            String sql = "SELECT COUNT(*) FROM " + tableName;
            PreparedStatement preparedStatement = connection.prepareStatement(sql);
            ResultSet resultSet = preparedStatement.executeQuery();
            if (resultSet.next()) {
                return resultSet.getInt(1) > 0;
            }
        } catch (SQLException e) {
            System.out.println("Error al verificar registros en la tabla. No se pudo establecer una conexión con la base de datos. " + tableName + ": " + e.getMessage());
        }
        return false;
    }

    public boolean checkRecords(String tableName) {
        if (!hasRecords(tableName)) {
            System.out.println("Error, no hay registros en la base de datos. Primero debe ingresar datos.");
            return false; // Retorna false si no hay registros
        }
        return true; // Retorna true si hay registros
    }

    public Connection getConnection() {
        return connection;
    }

    // Método para cerrar la conexión
    public void closeConnection() {
        if (connection != null) {
            try {
                connection.close();
                System.out.println("Conexión finalizada.");
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
    }
}
