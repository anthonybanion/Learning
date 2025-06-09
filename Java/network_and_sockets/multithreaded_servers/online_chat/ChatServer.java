/**
 * 
 * This code implements a simple multithreaded chat server in Java.
 * 
 * File: ChatServer.java
 * Author: Anthony Bañon
 * Created: 2025-05-29
 * Last Updated: 2025-05-29
 */


package network_and_sockets.multithreaded_servers.online_chat;

import java.io.*;
import java.net.*;
import java.util.*;

public class ChatServer {
    private static final int PORT = 12345;  // Change this to the desired port number
    // A set to hold all connected client handlers
    private static Set<ClientHandler> clientHandlers = Collections.synchronizedSet(new HashSet<>());
    // A counter to assign unique usernames to clients
    private static int userId = 1;
    // A server socket to listen for incoming connections
    private static ServerSocket serverSocket;
    

    public static void main(String[] args) {
        System.out.println("Chat Server started...");
        
        // Start a thread to listen for shutdown command
        new Thread(() -> {
            Scanner scanner = new Scanner(System.in);
            while (true) {  // Listen for shutdown command
                String input = scanner.nextLine();
                // If the input is "/shutdown", shut down the server
                if (input.equalsIgnoreCase("/shutdown")) {
                    shutdownServer();
                    break;
                }
            }
            scanner.close();
        }).start();

        // Start the server and accept client connections
        try (ServerSocket serverSocket = new ServerSocket(PORT)) {
            while (true) {
                Socket socket = serverSocket.accept();  // Accept a new client connection
                String username = "User" + userId++;
                // Create a new ClientHandler for the connected client
                ClientHandler clientHandler = new ClientHandler(socket, username);
                clientHandlers.add(clientHandler);  // Add the client handler to the set
                clientHandler.start();  // Start the client handler thread
                // Broadcast a message to all clients that a new user has joined
                broadcast(">> " + username + " joined the chat.");
            }
        } catch (IOException e) {
            System.err.println("Server error: " + e.getMessage());
        }
    }

    // Broadcast a message to all connected clients
    public static void broadcast(String message) {
        synchronized (clientHandlers) {
            for (ClientHandler client : clientHandlers) {
                client.sendMessage(message);
            }
        }
    }

    // Remove a client handler when a client disconnects
    public static void removeClient(ClientHandler client) {
        clientHandlers.remove(client);
        broadcast(">> " + client.getUsername() + " left the chat.");
    }

    // Shutdown the server and close all connections
     public static void shutdownServer() {
        System.out.println(">> Shutting down server...");
        broadcast(">> Server is shutting down.");

        // Close all client connections
        synchronized (clientHandlers) {
            // Notify all clients about the shutdown
            for (ClientHandler client : clientHandlers) {
                client.sendMessage(">> Connection closed by server.");
                client.closeConnection();
            }
            clientHandlers.clear();
        }

        // Close the server socket
        try {
            if (serverSocket != null && !serverSocket.isClosed()) {
                serverSocket.close();
            }
        } catch (IOException e) {
            System.err.println("Error closing server socket: " + e.getMessage());
        }

        System.out.println(">> Server shut down successfully.");
        System.exit(0);
    }
}
