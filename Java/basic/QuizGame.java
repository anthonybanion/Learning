/* Brief: A simple quiz game.
 * Detail: I use switch-case statements to check the user's answers.
 * Date:  04/02/2020
 * Version: 1.0
 */
import java.util.Scanner;

public class QuizGame {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int score = 0; // Counter for correct answers
        String answer; // User's answer

        System.out.println("Welcome to the Quiz Game!\n");

        // Question 1
        System.out.println("1. What is the capital of France?");
        System.out.println("A. Berlin");
        System.out.println("B. Madrid");
        System.out.println("C. Paris");
        System.out.println("D. Rome");
        System.out.print("Enter your answer (A, B, C, D): ");
        answer = scanner.next().toUpperCase(); // Convert input to uppercase for consistency

        // Check answer using switch-case
        switch (answer) {
            case "C":
                System.out.println("Correct!\n");
                score++;
                break;
            case "A":
            case "B":
            case "D":
                System.out.println("Wrong! The correct answer is C.\n");
                break;
            default:
                System.out.println("Invalid input. No points awarded.\n");
        }

        // Question 2
        System.out.println("2. Which planet is known as the Red Planet?");
        System.out.println("A. Earth");
        System.out.println("B. Mars");
        System.out.println("C. Jupiter");
        System.out.println("D. Venus");
        System.out.print("Enter your answer (A, B, C, D): ");
        answer = scanner.next().toUpperCase();

        switch (answer) {
            case "B":
                System.out.println("Correct!\n");
                score++;
                break;
            case "A":
            case "C":
            case "D":
                System.out.println("Wrong! The correct answer is B.\n");
                break;
            default:
                System.out.println("Invalid input. No points awarded.\n");
        }

        // Question 3
        System.out.println("3. Who wrote 'To Kill a Mockingbird'?");
        System.out.println("A. Harper Lee");
        System.out.println("B. J.K. Rowling");
        System.out.println("C. Mark Twain");
        System.out.println("D. Ernest Hemingway");
        System.out.print("Enter your answer (A, B, C, D): ");
        answer = scanner.next().toUpperCase();

        switch (answer) {
            case "A":
                System.out.println("Correct!\n");
                score++;
                break;
            case "B":
            case "C":
            case "D":
                System.out.println("Wrong! The correct answer is A.\n");
                break;
            default:
                System.out.println("Invalid input. No points awarded.\n");
        }
        
        // Question 4
        System.out.println("4. What is the largest ocean on Earth?");
        System.out.println("A. Atlantic");
        System.out.println("B. Indian");
        System.out.println("C. Arctic");
        System.out.println("D. Pacific");
        System.out.print("Enter your answer (A, B, C, D): ");
        answer = scanner.next().toUpperCase();

        switch (answer) {
            case "D":
                System.out.println("Correct!\n");
                score++;
                break;
            case "A":
            case "B":
            case "C":
                System.out.println("Wrong! The correct answer is D.\n");
                break;
            default:
                System.out.println("Invalid input. No points awarded.\n");
        }

        // Question 5
        System.out.println("5. Which element has the chemical symbol 'O'?");
        System.out.println("A. Oxygen");
        System.out.println("B. Gold");
        System.out.println("C. Silver");
        System.out.println("D. Hydrogen");
        System.out.print("Enter your answer (A, B, C, D): ");
        answer = scanner.next().toUpperCase();

        switch (answer) {
            case "A":
                System.out.println("Correct!\n");
                score++;
                break;
            case "B":
            case "C":
            case "D":
                System.out.println("Wrong! The correct answer is A.\n");
                break;
            default:
                System.out.println("Invalid input. No points awarded.\n");
        }

        // Calculate and display final score
        double percentage = (score / 5.0) * 100;
        System.out.println("You scored " + score + " out of 5.");
        System.out.printf("Your final score is %.2f%%\n", percentage);

        scanner.close(); // Close scanner to prevent resource leaks
    }
}
