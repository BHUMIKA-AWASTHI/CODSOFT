import tkinter as tk
from tkinter import ttk, messagebox
import datetime

class ToDoList:
    def __init__(self, root):
        self.root = root
        self.tasks = []
        self.task_list = tk.Listbox(root, width=40, height=10)
        self.task_list.pack(padx=10, pady=10)

        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(padx=10, pady=10)

        self.due_date_entry = tk.Entry(root, width=40)
        self.due_date_entry.pack(padx=10, pady=10)

        self.priority_var = tk.StringVar()
        self.priority_var.set("normal")
        self.priority_menu = ttk.OptionMenu(root, self.priority_var, "normal", "high", "normal", "low")
        self.priority_menu.pack(padx=10, pady=10)

        self.create_task_button = tk.Button(root, text="Create Task", command=self.create_task)
        self.create_task_button.pack(padx=10, pady=10)

        self.update_task_button = tk.Button(root, text="Update Task", command=self.update_task)
        self.update_task_button.pack(padx=10, pady=10)

        self.delete_task_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_task_button.pack(padx=10, pady=10)

        self.mark_completed_button = tk.Button(root, text="Mark Completed", command=self.mark_completed)
        self.mark_completed_button.pack(padx=10, pady=10)

        self.sort_tasks_button = tk.Button(root, text="Sort Tasks", command=self.sort_tasks)
        self.sort_tasks_button.pack(padx=10, pady=10)

        self.reminder_time = "09:00"  # default reminder time

    def create_task(self):
        task = self.task_entry.get()
        due_date = self.due_date_entry.get()
        priority = self.priority_var.get()
        self.tasks.append({"task": task, "due_date": due_date, "priority": priority, "completed": False})
        self.task_list.insert(tk.END, task)
        self.task_entry.delete(0, tk.END)
        self.due_date_entry.delete(0, tk.END)

    def update_task(self):
        selected_task = self.task_list.curselection()
        if selected_task:
            task = self.task_entry.get()
            due_date = self.due_date_entry.get()
            priority = self.priority_var.get()
            self.tasks[selected_task[0]]["task"] = task
            self.tasks[selected_task[0]]["due_date"] = due_date
            self.tasks[selected_task[0]]["priority"] = priority
            self.task_list.delete(selected_task[0])
            self.task_list.insert(selected_task[0], task)
            self.task_entry.delete(0, tk.END)
            self.due_date_entry.delete(0, tk.END)

    def delete_task(self):
        selected_task = self.task_list.curselection()
        if selected_task:
            self.tasks.pop(selected_task[0])
            self.task_list.delete(selected_task[0])

    def mark_completed(self):
        selected_task = self.task_list.curselection()
        if selected_task:
            self.tasks[selected_task[0]]["completed"] = True
            self.task_list.delete(selected_task[0])
            self.task_list.insert(selected_task[0], f"{self.tasks[selected_task[0]]['task']} (Completed)")

    def sort_tasks(self):
        self.tasks.sort(key=lambda x: x["priority"])
        self.task_list.delete(0, tk.END)
        for task in self.tasks:
            self.task_list.insert(tk.END, task["task"])

    def set_reminder(self):
        current_time = datetime.datetime.now().strftime("%H:%M")
        if current_time == self.reminder_time:
            for task in self.tasks:
                if task["due_date"] and task["due_date"] < datetime.date.today():
                    messagebox.showinfo("Reminder", f"Reminder: {task['task']}")

    def run(self):
        self.root.after(1000, self.set_reminder)  # check for reminders every 1 second
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("To-Do List")
    todo_list = ToDoList(root)
    todo_list.run()