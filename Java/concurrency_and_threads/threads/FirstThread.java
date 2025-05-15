/**
 * 
 * Description: This program demonstrates the creation of a thread in Java 
 *              by extending the Thread class.
 * 
 * File: FirstThread.java 
 * Author: Anthony Bañon
 * Created: 2025-05-01
 * Last Updated: 2025-05-01
 */



package concurrency_and_threads.threads;
import java.lang.Thread;

public class FirstThread extends Thread {
    public void run() {
        // This method is executed when the thread is started
        System.out.println("Hello from the thread!");
    }

    public static void main(String[] args) {
        FirstThread hilo = new FirstThread();
        hilo.start(); //Creates and launches a new thread that executes run()
        // The main thread continues executing
        System.out.println("Hello from the main thread!");
    }
}
