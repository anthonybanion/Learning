/**
 * 
 * This code implements a ClientHandler class for a 
 * simple multithreaded chat server in Java.
 * 
 * File: ClientHandler.java
 * Author: Anthony Bañon
 * Created: 2025-05-29
 * Last Updated: 2025-05-29
 */


package network_and_sockets.multithreaded_servers.online_chat;
import java.io.*;
import java.net.*;


class ClientHandler extends Thread {
    private Socket socket;
    private String username;
    private PrintWriter out;
    private BufferedReader in;
    
    // Constructor to initialize the ClientHandler with a socket and username
    public ClientHandler(Socket socket, String username) {
        this.socket = socket;
        this.username = username;
    }

    public String getUsername() {
        return username;
    }

    // Method to broadcast messages to all connected clients
    public void run() {
        try {  // Initialize input and output streams for the socket
            in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            // PrintWriter for sending messages to the client
            out = new PrintWriter(socket.getOutputStream(), true);

            String msg;
            // Notify the client of their username
            while ((msg = in.readLine()) != null) {
                ChatServer.broadcast(username + ": " + msg);
            }
        } catch (IOException e) {
            System.err.println(username + " disconnected.");
        } finally {
            try { socket.close(); } catch (IOException ignored) {}
            ChatServer.removeClient(this);
        }
    }

    public void sendMessage(String message) {
        if (out != null) {
            out.println(message);
        }
    }

    public void closeConnection() {
    try {
        if (socket != null && !socket.isClosed()) {
            socket.close();
        }
    } catch (IOException e) {
        e.printStackTrace();
    }
}
}

