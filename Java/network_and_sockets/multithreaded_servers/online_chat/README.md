# 🧠 Online Chat Application (Java)

## 📌 Assignment Title: _Online Chat Application_

This assignment aims to assess your skills in **socket programming**, **client-server communication**, and **user interface design** in Java.

---

## 📋 Assignment Instructions

You are tasked with developing a simple online chat application using Java. The application should allow **multiple users to connect to a central server**, send messages, and receive messages from other users.

---

## ✅ Requirements

### 🖥️ Server Implementation

- **ChatServer.java** must:
  - Use socket programming to manage connections from multiple clients.
  - Handle incoming client connections.
  - Assign a **unique user ID** to each connected client.
  - Maintain a list of connected users.
  - Broadcast messages to all clients.

### 💬 Client Implementation

- **ChatClient.java** must:
  - Connect to the server using sockets.
  - Allow the user to **send messages** to the server.
  - Display **incoming messages** from other users.
  - Be responsive and run on a separate thread for listening.

### 🧑‍💻 User Interface

- A **text-based UI** for the client that:
  - Lets the user input and send messages.
  - Displays messages from other users in real-time.

---

## 🛠️ How to Run

> 📌 Requirements: JDK 8 or higher, terminal or console

#### 1. Compile the files

```bash
javac ChatServer.java
javac ChatClient.java
```

#### 2. Run the server

In one terminal window:

```
java ChatServer
```

#### 3. Run one or more clients

In separate terminal windows:

```bash
    java ChatClient
```

#### 4. Chat away!

Type a message and press Enter. It will be broadcast to all connected users.

#### 5. Stop the server

When you want to stop the server, go back to the server terminal and type:

```bash
    /shutdown
```

This command gracefully closes the server and disconnects all users.

## 📷 Screenshot: Text-based Interface

- Client shows messages from all users
- Input is handled in the same console window

## 📂 Project Structure

```text
Java/
└── network_and_sockets/
    └── multithreaded_servers/
        └── OnlineChat/
            ├── ChatServer.java
            ├── ChatClient.java
            ├── screenshot.png
            └── README.md
```

## 🔍 Implementation Overview

This project uses TCP sockets for communication and multithreading on the server side to manage multiple clients concurrently.

- ChatServer uses a ServerSocket to listen for connections and spins off a new thread for each client.
- Each client connects using a Socket and has a dedicated listener thread to receive incoming messages.
- A synchronized list is used to manage all connected clients and ensure proper broadcasting.
- The client interface is purely console-based, allowing for minimalist and fast interaction.

## 💡 Key Concepts

- **Sockets in Java:** ServerSocket and Socket are used for establishing connections.
- **Multithreading:** Each client runs in a separate thread on the server using Runnable.
- **Broadcasting:** Server sends received messages to all connected clients using output streams.
- **Console I/O:** Scanner is used for user input and System.out.println() for output.

## 📚 References

- Oracle Java Documentation. (n.d.). Java Platform, Standard Edition 8 API Specification. Retrieved from https://docs.oracle.com/javase/8/docs/api/
- Deitel, P. J., & Deitel, H. M. (2017). Java: How to Program, Early Objects (11th ed.). Pearson.
- Liang, Y. D. (2019). Introduction to Java Programming and Data Structures (12th ed.). Pearson.
- Oracle. (n.d.). Java Tutorials: Custom Networking. Retrieved from https://docs.oracle.com/javase/tutorial/networking/sockets/
