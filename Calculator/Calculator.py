import tkinter as tk

number = ""
def add_to_calculation(num):
    global number
    number += num
    output_box.delete(1.0, "end")
    output_box.insert(1.0,number)

def evaluate():
    global number
    try:
        numbers = eval(number)
        numbers = int(numbers) if numbers == int(numbers) else numbers
        output_box.delete(1.0, "end")
        output_box.insert(1.0, str(numbers))
    except ZeroDivisionError:
        clear_text()
        output_box.insert(1.0, "Error")

def clear_text():
    global number
    number = ""
    output_box.delete(1.0, "end")

def back_button():
    global number
    num = number[0:-1]
    number = num
    output_box.delete(1.0, "end")
    output_box.insert(1.0, number)


# create window
window = tk.Tk()
window.title("Calculator")
window.geometry("300x548")
window.resizable(height=False, width=False)

# add background image
calculator_img = tk.PhotoImage(file="Calculator.png")
bg_image = tk.Label(master=window, image=calculator_img)
bg_image.pack()

# create output box
output_box = tk.Text(master=window, width=18, height=3, background="black", bd=0, fg="white", font="Arial 19",  highlightthickness=0)
output_box.place(x= 23,y= 97)


# create button
button_clear= tk.Button(master=window, text= "AC", width=4, height=1, font= "Arial 15", command=clear_text)
button_clear.place(x= 25,y= 230)
button_open= tk.Button(master=window, text= "(", width=4, height=1, font= "Arial 15", command=lambda :add_to_calculation("("))
button_open.place(x= 90,y= 230)
button_close= tk.Button(master=window, text= ")", width=4, height=1, font= "Arial 15", command=lambda :add_to_calculation(")"))
button_close.place(x= 155,y= 230)


button_7= tk.Button(master=window, text= "7", width=4, height=1, font= "Arial 15", command=lambda :add_to_calculation("7"))
button_7.place(x= 25,y= 282)
button_8= tk.Button(master=window, text= "8", width=4, height=1, font= "Arial 15", command=lambda :add_to_calculation("8"))
button_8.place(x= 90,y= 282)
button_9= tk.Button(master=window, text= "9", width=4, height=1, font= "Arial 15", command=lambda :add_to_calculation("9"))
button_9.place(x= 155,y= 282)

button_4= tk.Button(master=window, text= "4", width=4, height=1, font= "Arial 15", command=lambda :add_to_calculation("4"))
button_4.place(x= 25,y= 334)
button_5= tk.Button(master=window, text= "5", width=4, height=1, font= "Arial 15", command=lambda :add_to_calculation("5"))
button_5.place(x= 90,y= 334)
button_6= tk.Button(master=window, text= "6", width=4, height=1, font= "Arial 15", command=lambda :add_to_calculation("6"))
button_6.place(x= 155,y= 334)

button_1= tk.Button(master=window, text= "1", width=4, height=1, font= "Arial 15", command=lambda :add_to_calculation("1"))
button_1.place(x= 25,y= 386)
button_2= tk.Button(master=window, text= "2", width=4, height=1, font= "Arial 15", command=lambda :add_to_calculation("2"))
button_2.place(x= 90,y= 386)
button_3= tk.Button(master=window, text= "3", width=4, height=1, font= "Arial 15", command=lambda :add_to_calculation("3"))
button_3.place(x= 155,y= 386)

button_0= tk.Button(master=window, text= "0", width=4, height=1, font= "Arial 15", command=lambda :add_to_calculation("0"))
button_0.place(x= 90,y= 438)
button_dot= tk.Button(master=window, text= ".", width=4, height=1, font= "Arial 15", command=lambda :add_to_calculation("."))
button_dot.place(x= 25,y= 438)
button_equal= tk.Button(master=window, text= "=", width=4, height=1, font= "Arial 15", command=evaluate)
button_equal.place(x= 155,y= 438)

button_plus= tk.Button(master=window, text= "+", width=4, height=1, font= "Arial 15", command=lambda :add_to_calculation("+"))
button_plus.place(x= 220,y= 438)
button_minas= tk.Button(master=window, text= "-", width=4, height=1, font= "Arial 15", command=lambda :add_to_calculation("-"))
button_minas.place(x= 220,y= 386)
button_multi= tk.Button(master=window, text= "*", width=4, height=1, font= "Arial 15", command=lambda :add_to_calculation("*"))
button_multi.place(x= 220,y= 334)
button_divide= tk.Button(master=window, text= "/", width=4, height=1, font= "Arial 15", command=lambda :add_to_calculation("/"))
button_divide.place(x= 220,y= 282)
button_percent= tk.Button(master=window, text= "←", width=4, height=1, font= "Arial 15", command= back_button)
button_percent.place(x= 220,y= 230)

window.mainloop()