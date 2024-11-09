/* Brief: Java program that shows information about the movie Matrix
 * Date: 06/11/2024
 * Version: 1.0
 */


 import java.util.Scanner;


public class Movie {
    public static void main(String[] args) {
        Scanner keyboard = new Scanner(System.in);
        boolean includedInThePlan = false;
        
        String sinopsis ="""
                Matrix is a 1999 science fiction action film written and directed by the Wachowskis.
                """; 
        
        String typeOfPlan = "plus";

        System.out.println("Enter the name of the movie: ");
        String movie = keyboard.nextLine();

        System.out.println("Please enter the release date of the movie: ");
        int releaseDate = keyboard.nextInt();

        System.out.println("What is the rating of the movie: ");
        double rating = keyboard.nextDouble();
        double media = (8.2 + rating + 9.0) /3;
        int calificaton = (int) (media/2);

        System.out.println("Welcome to Screen Mach");
        System.out.println("Movie " + movie);
        System.out.println("Release Date: " + releaseDate);
        System.out.println("Included in the Plan: " + includedInThePlan);
        System.out.println("Rating: " + rating);
        System.out.println("Media: " + media);
        System.out.println("Sinopsis: " + sinopsis);
        System.out.println("La calificación es: " + calificaton);

        if (releaseDate >= 2022){
            System.out.println("most popular movies");
        } else {
            System.out.println("Retro movies");
        }

        if(includedInThePlan && typeOfPlan.equals("plus")){
            System.out.println("Enjoy your movie");
        } else {
            System.out.println("movie not available on your current plan");
        }
    keyboard.close();
    }
}