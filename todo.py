import tkinter as tk
from tkinter import ttk

class ToDoList:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("To-Do List")
        self.root.geometry("500x300")  # Corrected the typo here

        self.tasks = []

        self.create_widgets()
        self.load_tasks()

        self.root.mainloop()

    def create_widgets(self):
        # Create task entry field
        self.task_entry = ttk.Entry(self.root)
        self.task_entry.pack(pady=10)

        # Create add task button
        self.add_task_button = ttk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_task_button.pack(pady=10)

        # Create task list frame
        self.task_list_frame = ttk.Frame(self.root)
        self.task_list_frame.pack(pady=10)

        # Create scrollbar for task list
        self.task_list_scrollbar = ttk.Scrollbar(self.task_list_frame, orient="vertical")
        self.task_list_scrollbar.pack(side="right", fill="y")

        # Create task list
        self.task_list = tk.Listbox(self.task_list_frame, yscrollcommand=self.task_list_scrollbar.set)
        self.task_list.pack(side="left", fill="both", expand=True)

        # Bind scrollbar to task list
        self.task_list_scrollbar.config(command=self.task_list.yview)

        # Create remove task button
        self.remove_task_button = ttk.Button(self.root, text="Remove Task", command=self.remove_task)
        self.remove_task_button.pack(pady=10)

        # Create mark task as done button
        self.mark_task_as_done_button = ttk.Button(self.root, text="Mark Task as Done", command=self.mark_task_as_done)
        self.mark_task_as_done_button.pack(pady=10)

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            self.task_entry.delete(0, tk.END)
            self.update_task_list()

    def remove_task(self):
        selected_index = self.task_list.curselection()
        if selected_index:
            task = self.tasks[selected_index[0]]
            self.tasks.remove(task)
            self.update_task_list()
    def mark_task_as_done(self):
        selected_index = self.task_list.curselection()
        if selected_index:
            task = self.tasks[selected_index[0]]
            self.tasks.remove(task)
            self.update_task_list()
            # Add task to done tasks list (not implemented in this code)

    def update_task_list(self):
        self.task_list.delete(0, tk.END)
        for task in self.tasks:
            self.task_list.insert(tk.END, task)

    def load_tasks(self):
        # Load tasks from a file or database (not implemented in this code)
        pass

    def save_tasks(self):
        # Save tasks to a file or database (not implemented in this code)
        pass

if __name__ == "__main__":
    app = ToDoList()