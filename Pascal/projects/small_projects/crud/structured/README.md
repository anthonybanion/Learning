# 🧠 Structured CRUD in Pascal

Welcome to the **structured implementation** of the Pascal CRUD project.  
This version follows a **procedural and modular** approach to organizing logic, data access, and shared components, allowing for clarity and maintainability in a console-based environment.

## 🎯 Objectives

- Understand how to structure a Pascal project for CRUD operations.
- Practice clean code and modular design principles in Pascal.
- Understand how to connect Pascal programs to an SQLite database.
- Maintain clear separation between:
  - Logic (procedures)
  - Data access (repositories)
  - Services (high-level operations)
  - Shared types

## ⚙️ Technologies

| Tool                  | Description                                 |
| --------------------- | ------------------------------------------- |
| 🐘 Pascal             | Language used for the logic (`Free Pascal`) |
| 🛢️ SQLite             | Lightweight relational database             |
| 📦 SQLdb              | Pascal's unit for database connection       |
| 🧪 Lazarus (optional) | IDE to simplify compiling and debugging     |

---

## 📁 Folder Structure

```bash
structured/
├── procedural/              # Pure procedural logic for CRUD
│   ├── createUser.pas       # Procedure to create a new user
│   ├── readUser.pas         # Procedure to read user data
│   ├── updateUser.pas       # Procedure to update user data
│   ├── deleteUser.pas       # Procedure to delete user data
│   └── ...
├── database/                # Low-level database support
│   ├── dbConnection.pas     # Establish and close SQLite connection
│   ├── dbUtils.pas          # Helper functions (e.g., table checks, formatting)
│   └── schema.sql           # SQL script to initialize database schema
├── services/                # Application services and data models
│   ├── userService.pas      # Business logic for user CRUD operations
│   ├── userModel.pas        # Data structure for user representation
│   ├── userRepository.pas   # Direct DB access layer for users
│   ├── dbUtils.pas          # Reused DB utilities (shared across services)
│   └── dbConnection.pas     # Reused DB connection (if isolated from database/)
├── shared/                  # Common constants, types, and globals
│   └── global.pas           # Shared types and variables
├── LICENSE                  # MIT License
└── README.md                # Project overview (this file)
```

---

## 🚀 How to Compile

Compile from project root:

```bash
fpc ../../main.pas \
  -Fuprocedural \
  -Fudatabase \
  -Fuservices \
  -Fushared \
  -o:crud

```

> Ensure you’re running this from the structured/ directory, or adjust paths accordingly.

## 🧪 Run

```bash
./crud
```

## 🛠 Requirements

- ✅ Free Pascal Compiler (FPC)
- ✅ SQLite3 library installed (e.g., libsqlite3.so)
- Optional: Lazarus IDE

## 📌 Notes

- This version does not use object-oriented classes, but can be migrated to OOP.
- Useful for learning the foundations of modular software design in Pascal.
- All procedures and services are kept isolated by responsibility.

## 📄 License

[MIT License](../../../../../LICENSE) — free to use, modify and distribute.

---

<div align="right" style="font-size: 2em;">
    <a href="../README.md">⬅️ Back to CRUD</a>
</div>
