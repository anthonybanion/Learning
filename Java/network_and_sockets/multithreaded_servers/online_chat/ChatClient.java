/**
 * 
 * This is a simple chat client that connects to a multithreaded chat server.
 * 
 * File: ChatClient.java
 * Author: Anthony Bañon
 * Created: 2025-05-29
 * Last Updated: 2025-05-29
 */


package network_and_sockets.multithreaded_servers.online_chat;
import java.io.*;
import java.net.*;

public class ChatClient {
    private static final String SERVER_IP = "localhost";  // Change this to the server's IP address
    private static final int SERVER_PORT = 12345;  // Change this to the server's IP and port

    public static void main(String[] args) {
        try (Socket socket = new Socket(SERVER_IP, SERVER_PORT)) {  // Connect to the server
            // Create input and output streams for user input and server communication
            BufferedReader userInput = new BufferedReader(new InputStreamReader(System.in));
            // Create input and output streams for the socket
            BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            // PrintWriter for sending messages to the server
            PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
            
            // Start a new thread to listen for incoming messages from the server
            Thread receiveThread = new Thread(() -> {
                try {  // Listen for messages from the server
                    String msg;
                    while ((msg = in.readLine()) != null) {
                        System.out.println(msg);
                    }
                } catch (IOException e) {
                    System.out.println("Connection closed.");
                }
            });
            receiveThread.start();

            System.out.println("Connected to chat. Start typing:");
            String input;
            // Read user input and send it to the server
            while ((input = userInput.readLine()) != null) {
                out.println(input);
            }
        } catch (IOException e) {
            System.err.println("Connection failed: " + e.getMessage());
        }
    }
}
