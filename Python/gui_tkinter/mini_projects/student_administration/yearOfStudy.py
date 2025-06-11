#Briefa: year of study
#Date: 05/11/2024
#version: 1.0

import sqlite3

def open_connection():
    connection = sqlite3.connect('Python/gui_tkinter/mini_projects/student_administration/students.db')
    return connection

def create_year_of_study_table():
    connection = open_connection()
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS "yearOfStudy" (
                    "id" INTEGER NOT NULL UNIQUE,
                    "year" TEXT NOT NULL,
                    PRIMARY KEY("id" AUTOINCREMENT))''')
    connection.commit()
    connection.close()
    print("The table has been created")

def insert_default_years():
    connection = open_connection()
    cursor = connection.cursor()
    cursor.execute('''INSERT INTO yearOfStudy(id, year) VALUES("1","first"),("2","second"),("3","third")''')
    connection.commit()
    connection.close()

def list_years_of_study():
    connection = open_connection()
    cursor = connection.cursor()
    cursor.execute('''SELECT * FROM yearOfStudy''')
    result = cursor.fetchall()
    connection.commit()
    connection.close()
    return result

def delete_year_of_study(id):
    connection = open_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM yearOfStudy WHERE id = ?", (id,))
    connection.commit()
    connection.close()

# open_connection()
# create_year_of_study_table()
# list_years_of_study()
