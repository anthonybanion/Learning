# #Briefa: Create a CRUD with sqlite3
# #Date: 05/11/2024
# #version: 1.0

import sqlite3

def open_connection():
    connection = sqlite3.connect('Python/gui_tkinter/mini_projects/student_administration/students.db')
    return connection

def create_students_table():
    connection = open_connection()
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS "students" (
                    "id" INTEGER NOT NULL UNIQUE,
                    "first_name" TEXT NOT NULL,
                    "last_name" TEXT NOT NULL,
                    "dni" TEXT NOT NULL UNIQUE,
                    PRIMARY KEY("id" AUTOINCREMENT))''')

    connection.commit()
    connection.close()
    print("The table has been created")

def insert_student(id, first_name, last_name, dni):
    connection = open_connection()
    cursor = connection.cursor()
    cursor.execute('''INSERT INTO students VALUES(?,?,?,?)''', (id, first_name, last_name, dni))
    connection.commit()
    connection.close()

def list_students():
    connection = open_connection()
    cursor = connection.cursor()
    cursor.execute('''SELECT * FROM students''')
    result = cursor.fetchall()
    connection.commit()
    connection.close()
    return result

def delete_student(id):
    connection = open_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM students WHERE id = ?", (id,))
    connection.commit()
    connection.close()

def update_student(id, first_name, last_name, dni):
    connection = open_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE students SET first_name = ? WHERE id = ?", (first_name, id))
    cursor.execute("UPDATE students SET last_name = ? WHERE id = ?", (last_name, id))
    cursor.execute("UPDATE students SET dni = ? WHERE id = ?", (dni, id))
    connection.commit()
    connection.close()

def search_student(id):
    connection = open_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students WHERE id = ?", (id,))
    result = cursor.fetchall()
    connection.commit()
    connection.close()
    return result
