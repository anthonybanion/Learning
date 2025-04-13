package introduction.chapter2;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class FindAverage {
    public static void main(String[] args) {
        String name;      // Nombre del estudiante
        int exam1, exam2, exam3;  // Notas de los tres exámenes
        double average;   // Promedio de las notas

        try {
            File file = new File("testdata.txt");  // Especificar el archivo
            Scanner scanner = new Scanner(file);  // Crear un Scanner para leer el archivo

            name = scanner.nextLine();   // Leer la primera línea (nombre del estudiante)
            exam1 = scanner.nextInt();   // Leer las tres notas
            exam2 = scanner.nextInt();
            exam3 = scanner.nextInt();

            scanner.close();  // Cerrar el Scanner

            average = (exam1 + exam2 + exam3) / 3.0;  // Calcular el promedio

            System.out.printf("The average grade for %s was %1.1f%n", name, average);

        } catch (FileNotFoundException e) {
            System.out.println("Error: Archivo no encontrado.");
            e.printStackTrace();
        }
    }
}
