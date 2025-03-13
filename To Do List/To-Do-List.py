import tkinter as tk

tasks = []
index_count = None  # Keep track of the selected task index


def show_message(text, color):
    """Display a message with a specified color for 5 seconds."""
    message_label.config(text=text, fg=color)
    message_label.after(5000, lambda: message_label.config(text=""))


def add_task():
    """Add a new task to the list."""
    task_text = entry_task.get().strip()
    if task_text:
        tasks.append(task_text)
        task_list.insert(tk.END, f"{len(tasks)}. {task_text}")  # Add to the end of the list
        entry_task.delete(0, tk.END)
        show_message("Task added successfully!", "green")
    else:
        show_message("Please enter a valid task!", "red")


def on_task_select(event):
    """Handle task selection from the listbox."""
    global index_count
    try:
        index_count = task_list.curselection()[0]
        entry_task.delete(0, tk.END)
        entry_task.insert(0, tasks[index_count])
    except IndexError:
        index_count = None


def update_task():
    """Update the selected task with new text."""
    global index_count
    new_task_text = entry_task.get().strip()
    if index_count is not None and new_task_text:
        tasks[index_count] = new_task_text  # Update the task in the list
        task_list.delete(index_count)  # Remove the old task
        task_list.insert(index_count, f"{index_count + 1}. {new_task_text}")  # Insert the updated task
        entry_task.delete(0, tk.END)
        show_message("Task updated successfully!", "green")
    elif index_count is None:
        show_message("Please select a task to update!", "red")
    else:
        show_message("Please enter a valid task!", "red")


def delete_task():
    """Delete the selected task."""
    global index_count
    if index_count is not None:
        del tasks[index_count]
        task_list.delete(index_count)

        # Refresh the list with updated numbering
        task_list.delete(0, tk.END)
        for i, task in enumerate(tasks, start=1):
            task_list.insert(tk.END, f"{i}. {task}")

        entry_task.delete(0, tk.END)
        index_count = None
        show_message("Task deleted successfully!", "green")
    else:
        show_message("Please select a task to delete!", "red")


# Create Window
window = tk.Tk()
window.title("To-Do List")
window.geometry("300x310")
window.config(bg="#121212")

# Header Label
header_label = tk.Label(
    master=window, text="To-Do List",
    font="Arial 12",
    bg="#2C3E50", fg="#c0c2c0",
    bd=0, highlightthickness=0,
    width=43
)
header_label.pack()

# Task List Box
task_list = tk.Listbox(
    master=window,
    bg="#2C3E50", fg="#ffffff",
    bd=0, highlightthickness=0,
    selectbackground="#4CAF50",
    width=48
)
task_list.pack(pady="15px")
task_list.bind("<<ListboxSelect>>", on_task_select)

# Entry Box for Task Input
entry_task = tk.Entry(
    master=window,
    bg="#2C3E50", fg="#ffffff",
    bd=0, highlightthickness=0,
    width=48
)
entry_task.pack()

# Buttons Frame
btn_frame = tk.Frame(master=window, bg="#121212")
add_task_btn = tk.Button(
    master=btn_frame, text="Add Task",
    height=1, width=10, fg="#121212", bg="#4CAF50",
    command=add_task
)
update_task_btn = tk.Button(
    master=btn_frame, text="Update Task",
    height=1, width=10, fg="#121212", bg="#4CAF50",
    command=update_task
)
delete_task_btn = tk.Button(
    master=btn_frame, text="Delete Task",
    height=1, width=10, fg="#121212", bg="#c71829",
    command=delete_task  # Fixed missing command
)

# Pack Buttons
add_task_btn.pack(side="left")
update_task_btn.pack(padx=10, side="left")
delete_task_btn.pack(pady=10)
btn_frame.pack()

# Message Label
message_label = tk.Label(master=window, text="", bg="#121212")
message_label.pack()

# Run Application
window.mainloop()
