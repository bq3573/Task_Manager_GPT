import tkinter as tk
from tkinter import ttk

class TaskManager:

    def add_task(self):
        task = self.task_entry.get()
        date = self.date_entry.get()
        duration = self.duration_entry.get()
        self.tasks.append((task, date, duration))
        self.tasks_list.insert("end", f"{task} - {date} - {duration} hours")
        self.task_entry.delete(0, "end")
        self.date_entry.set("")
        self.duration_entry.delete(0, "end")

    def complete_task(self):
        selected_task = self.tasks_list.curselection()
        if selected_task:
            index = selected_task[0]
            self.tasks.pop(index)
            self.tasks_list.delete(index)

    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")

        # Create style
        self.style = ttk.Style(self.root)
        self.style.configure("TFrame", background="#333")
        self.style.configure("TButton", background="#333", foreground="black", font=("Arial", 10))
        self.style.configure("TLabel", background="#333", foreground="#fff", font=("Arial", 10))
        self.style.configure("TEntry", background="#fff", foreground="#333", font=("Arial", 10))
        self.style.configure("TCombobox", background="#fff", foreground="#333", font=("Arial", 10))

        # Create main frame
        self.main_frame = ttk.Frame(self.root, style="TFrame")
        self.main_frame.pack(expand=True, fill="both")

        self.tasks = []

        # Create widgets
        self.task_label = ttk.Label(self.main_frame, text="Enter a task:", style="TLabel")
        self.task_entry = ttk.Entry(self.main_frame, style="TEntry")
        self.date_label = ttk.Label(self.main_frame, text="Completion date:", style="TLabel")
        self.date_entry = ttk.Combobox(self.main_frame, values=["Today", "Tomorrow", "Next week", "Next month"], style="TCombobox")
        self.duration_label = ttk.Label(self.main_frame, text="Duration (hours):", style="TLabel")
        self.duration_entry = ttk.Entry(self.main_frame, style="TEntry")
        self.add_button = ttk.Button(self.main_frame, text="Add Task", command=self.add_task, style="TButton")
        self.tasks_list = tk.Listbox(self.main_frame)
        self.complete_button = ttk.Button(self.main_frame, text="Complete Task", command=self.complete_task, style="TButton")

        # Add widgets to the main frame
        self.task_label.pack(side="left", padx=5, pady=5)
        self.task_entry.pack(side="left", padx=5, pady=5)
        self.date_label.pack(side="left", padx=5, pady=5)
        self.date_entry.pack(side="left", padx=5, pady=5)
        self.duration_label.pack(side="left", padx=5, pady=5)
        self.duration_entry.pack(side="left", padx=5, pady=5)
        self.add_button.pack(side="left", padx=5, pady=5)
        self.tasks_list.pack(side="left", padx=10, pady=10)
        self.complete_button.pack(side="left", padx=5, pady=5)


# Create the main window
root = tk.Tk()

# Create the task manager
task_manager = TaskManager(root)

# Run the main loop
root.mainloop()
