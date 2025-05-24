/**
 * 
 * Command-line interface for managing a library catalog.
 * 
 * File: Main.java
 * Author: Anthony Bañon
 * Created: 2025-05-24
 * Last Updated: 2025-05-24
 */


package paradigm_oop.generics;

import java.util.Scanner;


// Command-line interface for library catalog
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Catalog<LibraryItem<String>> catalog = new Catalog<>();

        boolean exit = false;

        while (!exit) {
            System.out.println("\nLibrary Catalog Menu:");
            System.out.println("1. Add Item");
            System.out.println("2. Remove Item");
            System.out.println("3. View Catalog");
            System.out.println("4. Exit");
            System.out.print("Select an option: ");
            int choice = scanner.nextInt();
            scanner.nextLine(); // consume newline

            switch (choice) {
                case 1:
                    System.out.print("Enter title: ");
                    String title = scanner.nextLine();
                    System.out.print("Enter author: ");
                    String author = scanner.nextLine();
                    System.out.print("Enter item ID: ");
                    String id = scanner.nextLine();
                    System.out.print("Enter type (e.g., Book, DVD): ");
                    String type = scanner.nextLine();

                    LibraryItem<String> newItem = new LibraryItem<>(title, author, id, type);
                    catalog.addItem(newItem);
                    System.out.println("Item added.");
                    break;

                case 2:
                    System.out.print("Enter item ID to remove: ");
                    String removeId = scanner.nextLine();
                    if (catalog.removeItem(removeId)) {
                        System.out.println("Item removed.");
                    } else {
                        System.out.println("Item not found.");
                    }
                    break;

                case 3:
                    catalog.displayItems();
                    break;

                case 4:
                    exit = true;
                    break;

                default:
                    System.out.println("Invalid option.");
            }
        }
        scanner.close();
    }
}
