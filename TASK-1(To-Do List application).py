import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def add_task():
    task = task_entry.get()
    if task.strip() != "":
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task can't be empty!")

def delete_task():
    try:
        index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")

def complete_task():
    try:
        index = tasks_listbox.curselection()[0]
        task = tasks_listbox.get(index)
        tasks_listbox.delete(index)
        completed_listbox.insert(tk.END, task)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as completed!")

def clear_completed():
    completed_listbox.delete(0, tk.END)

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

root = tk.Tk()
root.title("To-Do App")

style = ttk.Style()
style.theme_use('clam')  # Choose a theme ('clam', 'alt', 'default', 'classic')

frame = ttk.Frame(root, padding=10)
frame.pack()

task_entry = ttk.Entry(frame, width=40, font=('Arial', 14))
task_entry.pack(side=tk.LEFT, padx=5, ipady=5)

add_button = ttk.Button(frame, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT, padx=5, ipady=3)

buttons_frame = ttk.Frame(root, padding=5)
buttons_frame.pack()

delete_button = ttk.Button(buttons_frame, text="Delete Task", command=delete_task)
delete_button.pack(side=tk.LEFT, padx=5, pady=5)

complete_button = ttk.Button(buttons_frame, text="Mark as Completed", command=complete_task)
complete_button.pack(side=tk.LEFT, padx=5, pady=5)

clear_button = ttk.Button(root, text="Clear Completed", command=clear_completed)
clear_button.pack(pady=5)

tasks_listbox = tk.Listbox(root, width=50, height=10, font=('Arial', 12))
tasks_listbox.pack(pady=5)

completed_listbox = tk.Listbox(root, width=50, height=5, font=('Arial', 12), bg="#D3D3D3", selectbackground="#87CEFA")
completed_listbox.pack()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
