#Brief: task management
#Description: Designing a task management, the user should be able to create, update, mark as completed, and list pending tasks
#Date: 06/11/2024
#Version: 1.0

import datetime

class Task:
    def __init__(self, name, description, status):
        self.name = name
        self.description = description
        self.deadline= datetime.date.today()  # Deadline is set to today's date
        self.status = status

    def __str__(self):
        return f"{self.name}, {self.description}, {self.deadline}, {self.status}"
    
    def task_completed(self):
        self.status = "Completed"
        return self.status
    
class TaskManager:
    def __init__(self):
        self.tasks = []  # List to store tasks

    def add_task(self, task):  
        self.tasks.append(task)
        print(f"Task '{task.name}' added to the task list.")

    def search_by_deadlinbe(self, name):
        found = [task for task in self.tasks if task.name.lower() == name.lower()]  # Search for task by name
        print(f"Task '{name}' found in the task list.")
        for task in found:
            print(task)
        return 

    def delete_task(self, name):
        for task in self.tasks:
            if task.name.lower() == name.lower():
                self.tasks.remove(task)
                print(f"Task '{name}' deleted from the task list.")
                return
        print(f"Task '{name}' not found in the task list.")

    def show_tasks(self):
        if self.tasks:
            print("Tasks :")
            for task in self.tasks:
                print(task)
        else:
            print("No tasks in the task list.")

task1 = Task("Estudy", "Study for exam", "Pending")
task2 = Task("Buy", "Buy materials", "Pending")
task3 = Task("projects", "Deliver final project", "Pending")

task_manager = TaskManager()
task_manager.add_task(task1)
task_manager.add_task(task2)
task_manager.add_task(task3)

task_manager.show_tasks()

task1.task_completed()
task_manager.show_tasks()

task_manager.search_by_deadlinbe("Estudy")
task_manager.delete_task("Estudy")
task_manager.show_tasks()