/* Brief: Java program that shows information about the movie Matrix
 * Date: 06/11/2024
 * Version: 1.0
 */



public class Movie {
    public static void main(String[] args) {
        System.out.println("Welcome to Screen Mach");
        System.out.println("Movie Matrix");

        int releaseDate = 1999;
        boolean includedInThePlan = true;
        double rating = 8.7;
        double media = (8.2 + 6.0 + 9.0) /3;
        String sinopsis ="""
                Matrix is a 1999 science fiction action film written and directed by the Wachowskis.
                """; 
        System.out.println("Release Date: " + releaseDate);
        System.out.println("Included in the Plan: " + includedInThePlan);
        System.out.println("Rating: " + rating);
        System.out.println("Media: " + media);
        System.out.println("Sinopsis: " + sinopsis);



    }
}