# 🐘 CRUD with Pascal & SQLite

Welcome to the **Pascal CRUD Project**! This repository demonstrates how to build a full CRUD (Create, Read, Update, Delete) system using the **Pascal programming language** and **SQLite** as the database engine.

The project is designed to be a learning resource and includes two versions:

- 🧠 **Procedural Programming**: A step-by-step, structured approach.
- 🧱 **Object-Oriented Programming (OOP)**: A modular, scalable version for maintainable software.

---

## 🎯 Objectives

- Understand how to connect Pascal programs to an SQLite database.
- Learn how to perform **CRUD operations** using both **procedural** and **object-oriented** paradigms.
- Build a simple yet functional database-driven application.
- Practice clean code and modular design in Pascal.

---

## ⚙️ Technologies

| Tool                  | Description                                 |
| --------------------- | ------------------------------------------- |
| 🐘 Pascal             | Language used for the logic (`Free Pascal`) |
| 🛢️ SQLite             | Lightweight relational database             |
| 📦 SQLdb              | Pascal's unit for database connection       |
| 🧪 Lazarus (optional) | IDE to simplify compiling and debugging     |

---

## 🗂️ Project Structure

```bash
crud/
├── procedural/              # 💡 Procedural implementation
│   ├── main.pas             # Main program file
│   ├── db_connection.pas    # SQLite connection handling
│   ├── crud_operations.pas  # Create, Read, Update, Delete logic
│   └── schema.sql           # SQL script to create database structure
│
├── oop/                     # 🧱 Object-Oriented implementation
│   ├── main.pas
│   ├── database.pas         # Database connection class
│   ├── user.pas             # User class (domain model)
│   ├── user_repository.pas  # Class for CRUD operations on users
│   └── schema.sql
│
├── database/                # 🗃️ SQLite files and backups
│   └── users.db             # SQLite database file
│
├── docs/                    # 📚 Documentation (optional)
│   └── README.pdf
│
├── LICENSE                  # 📄 MIT License
└── README.md                # 📘 Project overview (this file)
```

---

## 🚀 How to Run

    This project requires Free Pascal Compiler (FPC) and the sqlite3 library installed.

### 🧪 Compile & Run (Procedural)

```bash
cd procedural
fpc main.pas
./main
```

### 🧱 Compile & Run (OOP)

```bash
cd oop
fpc main.pas
./main
```

---

## 🔓 License

This project is licensed under the MIT License.
Feel free to use, modify, and distribute it!

---

## 🤝 Contributing

Pull requests are welcome. If you find a bug or have an idea for improvement, feel free to open an issue or PR.

---

## 📌 Notes

- This is a console-based CRUD application.
- Ideal for those learning database programming with Pascal.
- The project will be expanded to support more entities and GUI options in the future.
