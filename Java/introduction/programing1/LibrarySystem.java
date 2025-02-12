import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class LibrarySystem {
    // Define the enumerated type for the book status (AVAILABLE or UNAVAILABLE)
    enum BookStatus {
        AVAILABLE, UNAVAILABLE
    }

    // 'library' is a HashMap where the key is the book title (String),
    // and the value is an array (Object[]) that holds the book's information.
    // Object[] is a generic array that can hold any type of object. Here it stores:
    // - The author (String),
    // - The quantity of books available (int),
    // - The book status (BookStatus, enum type)
    private static final Map<String, Object[]> library = new HashMap<>();
    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        while (true) { // Loop that keeps the program running until the user exits
            // Show the menu options for the user
            System.out.println("\nLibrary System:");
            System.out.println("1. Add Books");
            System.out.println("2. Borrow Books");
            System.out.println("3. Return Books");
            System.out.println("4. Exit");
            System.out.print("Choose an option: ");
            int choice = scanner.nextInt();
            scanner.nextLine(); // Consume the newline character

            try {
                switch (choice) { // Switch case to handle different user options
                    case 1:
                        // Adding a new book or updating quantity if the book already exists
                        System.out.print("Enter book title: ");
                        String addTitle = scanner.nextLine().toUpperCase(); // Convert title to uppercase
                        System.out.print("Enter author: ");
                        String author = scanner.nextLine();
                        System.out.print("Enter quantity: ");
                        int addQuantity = scanner.nextInt();
                        scanner.nextLine(); // Consume the newline character

                        if (library.containsKey(addTitle)) {
                            // If the book already exists, update the quantity
                            Object[] book = library.get(addTitle); // Retrieve the book's data
                            int newQuantity = (int) book[1] + addQuantity; // Add the new quantity to the existing one
                            book[1] = newQuantity; // Update the quantity in the Object[] array
                            System.out.println("Book quantity updated successfully!");
                        } else {
                            // If the book doesn't exist, add a new book
                            library.put(addTitle, new Object[]{author, addQuantity, BookStatus.AVAILABLE});
                            System.out.println("Book added successfully!");
                        }
                        break;

                    case 2:
                        // Borrowing a book
                        System.out.print("Enter book title: ");
                        String borrowTitle = scanner.nextLine().toUpperCase(); // Convert title to uppercase
                        System.out.print("Enter quantity to borrow: ");
                        int borrowQuantity = scanner.nextInt();
                        scanner.nextLine(); // Consume the newline character

                        // Check if the book exists and if there are enough copies to borrow
                        if (library.containsKey(borrowTitle)) {
                            Object[] book = library.get(borrowTitle); // Retrieve the book's data
                            int availableQuantity = (int) book[1]; // Get the available quantity of the book
                            if (availableQuantity >= borrowQuantity) {
                                book[1] = availableQuantity - borrowQuantity; // Update the quantity after borrowing
                                System.out.println("Book borrowed successfully!");
                            } else {
                                System.out.println("Not enough books available to borrow.");
                            }
                        } else {
                            System.out.println("Book not found in the library.");
                        }
                        break;

                    case 3:
                        // Returning a book
                        System.out.print("Enter book title: ");
                        String returnTitle = scanner.nextLine().toUpperCase(); // Convert title to uppercase
                        System.out.print("Enter quantity to return: ");
                        int returnQuantity = scanner.nextInt();
                        scanner.nextLine(); // Consume the newline character

                        // Check if the book exists in the library
                        if (library.containsKey(returnTitle)) {
                            Object[] book = library.get(returnTitle); // Retrieve the book's data
                            int availableQuantity = (int) book[1]; // Get the current quantity of the book
                            book[1] = availableQuantity + returnQuantity; // Update the quantity after returning
                            System.out.println("Book returned successfully!");
                        } else {
                            System.out.println("Book not found in the library.");
                        }
                        break;

                    case 4:
                        // Exit the program
                        System.out.println("Exiting the system. Goodbye!");
                        return; // Exit the program

                    default:
                        // Handle invalid input
                        System.out.println("Invalid choice. Please try again.");
                        break;
                }
            } catch (Exception e) {
                // Handle any exceptions (e.g., input errors)
                System.out.println("An error occurred: " + e.getMessage());
                scanner.nextLine(); // Consume the extra newline after an exception
            }
        }
    }
}
