/* Brief: This class is a simple example of a bank account
 * Date: 09/11/2024
 * Version: 1.0
*/
import java.util.Scanner;
public class Bancking {

    public static void login(String customer){
        Scanner keyboard = new Scanner(System.in);
        System.out.print("Enter your name: ");
        customer = keyboard.nextLine();
        System.out.println("Welcome " + customer);
        keyboard.close();
    }


    public static void showMenu() {
        System.out.println("Welcome to Banking");
        System.out.println("1. Check balance");
        System.out.println("2. Withdraw");
        System.out.println("3. Deposit");
        System.out.println("4. Exit");
        System.out.print("Enter an option: ");
    }

    public static void checkBalance(double availableBalance){
        System.out.println("Available balance: " + availableBalance);
    }

    public static double withdraw(double availableBalance, double withdraw){
        if (withdraw > availableBalance){
            System.out.println("Insufficient funds");
        } else {
            availableBalance -= withdraw;
        }
        return availableBalance;
    }

    public static void main(String[] arg){
        Scanner keyboard = new Scanner(System.in);
        String customer = " ";
        double availableBalance = 1599.99;
        int option = 0;
        login(customer);

        do{
            showMenu();
            option = keyboard.nextInt();
            switch(option){
                case 1:
                    checkBalance(availableBalance);
                    break;
                case 2:
                    System.out.print("Enter the amount to withdraw: ");
                    double withdraw = keyboard.nextDouble();
                    System.out.println("Available balance:" + withdraw(availableBalance, withdraw));
                    break;
                case 3:
                    System.out.print("Enter the amount to deposit: ");
                    double deposit = keyboard.nextDouble();
                    availableBalance += deposit;
                    checkBalance(availableBalance);
                    break;
                case 4:
                    System.out.println("Goodbye " + customer);
                    break;
                default:
                    System.out.println("Invalid option");
            }
        } while (option != 4);
    keyboard.close();
    }
}