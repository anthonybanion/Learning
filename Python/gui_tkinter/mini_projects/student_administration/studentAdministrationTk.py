# Description: Create a CRUD in a window with Tkinter
# Date: 05/11/2024
# Version: 1.0

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from studentAdministration import list_students, insert_student, search_student, update_student, delete_student
from yearOfStudy import list_years_of_study, create_year_of_study_table


def main():
    window = tk.Tk()
    window.title("Student Administration")
    window.geometry("600x400")
    
    notebook = ttk.Notebook(window)
    notebook.pack(fill='both', expand=True)

    tab_view_students = ttk.Frame(notebook)
    notebook.add(tab_view_students, text="View Students")
    
    tab_add_student = ttk.Frame(notebook)
    notebook.add(tab_add_student, text="Add Student")
    
    tab_search_student = ttk.Frame(notebook)
    notebook.add(tab_search_student, text="Search Student")

    def clear_input_fields(*entries):
        for entry in entries:
            entry.delete(0, tk.END)


    def display_students():
        columns = ("ID", "First Name", "Last Name", "DNI")
        student_table = ttk.Treeview(tab_view_students, columns=columns, show='headings')
        student_table.pack(pady=10, fill='both', expand=True)

        for col in columns:
            student_table.heading(col, text=col)
            student_table.column(col, width=100, anchor='center')

        def refresh_students():
            for item in student_table.get_children():
                student_table.delete(item)
            students = list_students()
            for student in students:
                student_table.insert("", tk.END, values=(student[0], student[1], student[2], student[3]))
            tab_add_student.after(1000, refresh_students)

        refresh_students()

    def add_student():
        tk.Label(tab_add_student, text="First Name:").grid(pady=5, row=0, column=0)
        tk.Label(tab_add_student, text="Last Name:").grid(pady=5, row=1, column=0)
        tk.Label(tab_add_student, text="DNI:").grid(pady=5, row=2, column=0)
        tk.Label(tab_add_student, text="Select Year of Study:").grid(pady=5, row=5, column=1)

        entry_first_name = tk.Entry(tab_add_student, width=40)
        entry_first_name.grid(padx=5, row=0, column=1)

        entry_last_name = tk.Entry(tab_add_student, width=40)
        entry_last_name.grid(padx=5, row=1, column=1)

        entry_dni = tk.Entry(tab_add_student, width=40)
        entry_dni.grid(padx=5, row=2, column=1)

        years = list_years_of_study()
        ttk.Combobox(tab_add_student, values=years).grid(pady=5, row=6, column=1)

        def save_student():
            first_name = entry_first_name.get()
            last_name = entry_last_name.get()
            dni = entry_dni.get()

            if first_name and last_name and dni:
                student_id = len(list_students()) + 1
                try:
                    insert_student(student_id, first_name, last_name, dni)
                    messagebox.showinfo("Success", "Student successfully added.")
                    # Clear the input fields after adding
                    clear_input_fields(entry_first_name, entry_last_name, entry_dni)
                    notebook.tab(tab_view_students, state="normal")
                    notebook.select(tab_view_students)
                except Exception as e:
                    messagebox.showerror("Error", f"An error occurred while adding the student: {e}")

        tk.Button(tab_add_student, text="Submit", width=50, command=save_student).grid(padx=10, pady=10, row=3, column=0, columnspan=2)

    def search_student_tab():
        tk.Label(tab_search_student, text="ID:").grid(pady=5, row=0, column=0)
        id_entry = tk.Entry(tab_search_student, width=40)
        id_entry.grid(padx=5, row=0, column=1)

        def perform_search():
            def modify_student():
                first_name = entry_first_name.get()
                last_name = entry_last_name.get()
                dni = entry_dni.get()
                if student_id and first_name:
                    try:
                        update_student(student_id, first_name, last_name, dni)
                        messagebox.showinfo("Success", "Student successfully updated.")
                        notebook.tab(tab_view_students, state="normal")
                        notebook.select(tab_view_students)
                        # Clear the entry fields after updating
                        clear_input_fields(entry_first_name, entry_last_name, entry_dni)

                    except Exception as e:
                        messagebox.showerror("Error", f"An error occurred while updating the student: {e}")

            def remove_student():
                if student_id:
                    try:
                        delete_student(student_id)
                        messagebox.showinfo("Success", "Student successfully deleted.")
                        notebook.tab(tab_view_students, state="normal")
                        notebook.select(tab_view_students)
                        # Clear the entry fields after deleting
                        clear_input_fields(entry_first_name, entry_last_name, entry_dni)
                    except Exception as e:
                        messagebox.showerror("Error", f"An error occurred while deleting the student: {e}")

            student_id = id_entry.get()
            if not student_id.isdigit():
                messagebox.showerror("Error", "Please enter a valid numeric ID.")
                id_entry.delete(0, tk.END)

                return

            student_id = int(student_id)
            students = search_student(student_id)

            if students:
                student = students[0]
                tk.Label(tab_search_student, text="First Name:").grid(pady=5, row=2, column=0)
                tk.Label(tab_search_student, text="Last Name:").grid(pady=5, row=3, column=0)
                tk.Label(tab_search_student, text="DNI:").grid(pady=5, row=4, column=0)

                entry_first_name = tk.Entry(tab_search_student, width=40)
                entry_first_name.insert(0, student[1])
                entry_first_name.grid(padx=5, row=2, column=1) 

                entry_last_name = tk.Entry(tab_search_student, width=40)
                entry_last_name.insert(0, student[2])
                entry_last_name.grid(padx=5, row=3, column=1)

                entry_dni = tk.Entry(tab_search_student, width=40)
                entry_dni.insert(0, student[3])
                entry_dni.grid(padx=5, row=4, column=1)

                tk.Button(tab_search_student, text="Update", width=50, command=modify_student).grid(padx=10, pady=10, row=5, column=0, columnspan=2)
                tk.Button(tab_search_student, text="Delete", width=50, command=remove_student).grid(padx=10, pady=10, row=6, column=0, columnspan=2)

            else:
                messagebox.showerror("Error", "Student not found.")
                

            id_entry.delete(0, tk.END)

        tk.Button(tab_search_student, text="Search", width=50, command=perform_search).grid(padx=10, pady=10, row=1, column=0, columnspan=2)

    display_students()
    add_student()
    search_student_tab()
    window.mainloop()


main()



