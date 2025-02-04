/*Brief: A simple quiz game.
 *Detail: I Use arrays to store questions and answers.
 *Date:  04/02/2020
 *Version: 1.0
 */
import java.util.Scanner;

public class Quiz {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int score = 0; // Variable to store the number of correct answers

        // Array of questions
        String[][] questions = {
            {"What is the capital of France?", "A. Berlin", "B. Madrid", "C. Paris", "D. Rome", "C"},
            {"Which planet is known as the Red Planet?", "A. Earth", "B. Mars", "C. Jupiter", "D. Venus", "B"},
            {"Who wrote 'To Kill a Mockingbird'?", "A. Harper Lee", "B. J.K. Rowling", "C. Mark Twain", "D. Ernest Hemingway", "A"},
            {"What is the largest ocean on Earth?", "A. Atlantic", "B. Indian", "C. Arctic", "D. Pacific", "D"},
            {"Which element has the chemical symbol 'O'?", "A. Oxygen", "B. Gold", "C. Silver", "D. Hydrogen", "A"}
        };

        System.out.println("Welcome to the Quiz Game!\n");

        // Loop through each question
        for (int i = 0; i < questions.length; i++) {
            System.out.println("Question " + (i + 1) + ": " + questions[i][0]);
            System.out.println(questions[i][1]);
            System.out.println(questions[i][2]);
            System.out.println(questions[i][3]);
            System.out.println(questions[i][4]);
            System.out.print("Enter your answer (A, B, C, D): ");

            String userAnswer = scanner.next().toUpperCase();

            // Validate input
            while (!userAnswer.equals("A") && !userAnswer.equals("B") && 
                   !userAnswer.equals("C") && !userAnswer.equals("D")) {
                System.out.print("Invalid input. Please enter A, B, C, or D: ");
                userAnswer = scanner.next().toUpperCase();
            }

            // Check if the answer is correct
            if (userAnswer.equals(questions[i][5])) {
                System.out.println("Correct!\n");
                score++;
            } else {
                System.out.println("Wrong! The correct answer was " + questions[i][5] + ".\n");
            }
        }

        // Calculate and display final score
        double percentage = (score / 5.0) * 100;
        System.out.println("You scored " + score + " out of 5.");
        System.out.printf("Your final score is %.2f%%\n", percentage);

        scanner.close();
    }
}
