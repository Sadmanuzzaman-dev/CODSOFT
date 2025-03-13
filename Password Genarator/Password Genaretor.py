import tkinter as tk
import ttkbootstrap as ttk
import random
import string

combined_list1 = (list(string.digits) + list(string.ascii_lowercase) + list(string.ascii_uppercase))

combined_list2 = (list(string.digits) + list(string.ascii_lowercase) + list(string.ascii_uppercase) + list("!@#$%&+-=[]{};',./<>~" ))

def simple_pass_generate():
    global combined_list1
    number = 0
    password = ""
    try:
        number = int(num.get())
    except ValueError:
        output_box.delete(0, tk.END)
        output_box.insert(tk.END, "Enter an Invalid input")

    for generate in range(0, number + 1):
        if generate > 0:
            random_number = random.choice(combined_list1)
            password += random_number

    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, password)
    output_box.config(fg="Orange")
    input_num.delete(0, tk.END)


def complex_pass_generate():
    global combined_list2
    number = 0
    password = ""
    try:
        number = int(num.get())
    except ValueError:
        output_box.delete(0, tk.END)
        output_box.insert(tk.END, "Enter an Invalid input")

    for generate in range(0, number+1):
        if generate > 0:
            random_number = random.choice(combined_list2)
            password += random_number

    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, password)
    output_box.config(fg= "Green")
    input_num.delete(0, tk.END)


def copy_pass():
    output_box.clipboard_clear()
    windows.clipboard_append(output_box.get("1.0", "end-1c"))
    windows.update()


def on_focus_in(event):
    if input_num.get() == "How many characters you want?":
        input_num.delete(0, tk.END)

def on_focus_out(event):
    if input_num.get() == "":
        input_num.insert(0, "How many characters you want?")


# Create a window
windows = ttk.Window(themename="superhero")
windows.title("Password Generator")
windows.geometry("400x260")


# Title
title = tk.Label(master=windows, text="Password Generator", font="Calibra 20", fg="black", pady="10px")
title.pack()


# Take user input
input_frame = tk.Frame(master= windows, pady="4px")
num = tk.StringVar()
input_num = tk.Entry(master= input_frame, width=30, textvariable=num, fg="Gray")
convert_btn1 = tk.Button(master= input_frame, text="Generate Weak Password", command=simple_pass_generate, width=25)
convert_btn2 = tk.Button(master= input_frame, text="Generate Complex Password", command=complex_pass_generate, width=25)
input_num.insert(0, "How many characters you want?")

input_num.bind("<FocusIn>", on_focus_in)
input_num.bind("<FocusOut>", on_focus_out)

input_num.pack(padx="5px")
convert_btn1.pack(pady="5px", padx="5px")
convert_btn2.pack(pady="2px" , )
input_frame.pack()


# Give output
output_frame = tk.Frame(master= windows, pady="20px" )
output_box = tk.Text(master=output_frame, font="Calibra 14", width=17, height=1)
copy_btn = tk.Button(master= output_frame, text="Copy", height=2, command=copy_pass, width=8)
output_box.pack(side="left", padx="5px")
copy_btn.pack(side="left")
output_frame.pack()


# Run the code
windows.mainloop()

