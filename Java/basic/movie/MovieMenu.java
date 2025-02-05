/* Brief: Java program that shows information about the movie Matrix
 * Date: 06/11/2024
 * Version: 1.0
 */


import java.util.Scanner;

public class MovieMenu {
    //function
    public static final int ACOUNT = 3;
    public static void showMenu() {
        System.out.println("Welcome to Screen Mach");
        System.out.println("1. Movie");
        System.out.println("2. Series");
        System.out.println("3. Exit");
        System.out.print("Enter an option: ");
    }

    public static void popularMovies(int releaseDate) {
           if (releaseDate >= 2022) {
            System.out.println("Most popular movies");
        } else {
            System.out.println("Retro movies");
        }
       
    }

    public static double average(){
        @SuppressWarnings("resource")
        Scanner keyboard = new Scanner(System.in);
        double gradeAverage = 0;
        for (int i = 0; i < ACOUNT; i++) {
            System.out.println("Please enter a rating: ");
            int rating = keyboard.nextInt();
            gradeAverage += rating;
        }
        gradeAverage /= ACOUNT;
        return gradeAverage;
    }

    public static void showMovieInfo(int option) {
        Scanner keyboard = new Scanner(System.in);
        System.out.println(option == 1 ? "Enter the name of the movie: " : "Enter the name of the series: ");
        String movie = keyboard.nextLine(); // Read the name of the movie
        System.out.print("Please enter the release date of the movie: ");
        int releaseDate = keyboard.nextInt();
        popularMovies(releaseDate);
        System.out.println("Average rating: " + average());
         System.out.println("Movie: " + movie);
        System.out.println("Release Date: " + releaseDate);
     keyboard.close();
    }




    public static void main(String[] args) {
        Scanner keyboard = new Scanner(System.in);
        int option = 0;
        
        do {
            showMenu();
            
            if (keyboard.hasNextInt()) {  // Check if the input is a number
                option = keyboard.nextInt();
                keyboard.nextLine(); // Clear the buffer
            } else {
                System.out.println("Invalid input! Please enter a valid number.");
                keyboard.nextLine(); // Clear the buffer
                continue;
            }
            
            switch (option) {
                case 1: {
                    showMovieInfo(option);
                    break;
                }
                case 2: {
                    showMovieInfo(option);
                    break;
                }
                case 3:
                    System.out.println("Exiting...");
                    break;
                default:
                    System.out.println("Invalid option, please choose a valid option.");
            }
        } while (option != 3); // Continue until option 3 is chosen

        keyboard.close();
    }
}
