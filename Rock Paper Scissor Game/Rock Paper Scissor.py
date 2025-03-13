import random
import tkinter as tk
from tkinter import StringVar

computer = 0
user = 0

def choice_winner(user_choice):
    global copm_choice
    global who_won
    global computer_score
    global user_score
    global computer
    global user



    your_choice.set(user_choice)
    choices = ["Rock", "Paper", "Scissor"]

    computer_choices = random.choice(choices)
    copm_choice.set(computer_choices)

    if user_choice == computer_choices:
        who_won.set("Tie")
    elif ( (user_choice == "Rock" and computer_choices == "Scissor")or
            (user_choice == "Paper" and computer_choices == "Rock") or
            (user_choice == "Scissor" and computer_choices == "Paper")):
        who_won.set("You Win")
        user += 1


    else:
        who_won.set("Computer Win")
        computer += 1

    computer_score.set(str(computer))
    user_score.set(str(user))



# Create window
window = tk.Tk()
window.geometry("300x280")
window.config(bg="#121212")
window.title("Rock-Paper-Scissor Game")


# Game name Display
game_name = tk.Label(master=window, bg="Gray", height=2, width=100, text="Rock-Paper-Scissor Game",
                                   font="Arial 15 bold", fg="Yellow")
game_name.pack(pady=2)


computer_frame = tk.Frame(master=window)

# Computer Score Display
computer_score = StringVar()
computer_score.set("0")
computer_score_display = tk.Label(master=window, bg="Red", height=1, width=5,
                                    font="Arial 15 bold", fg="White", textvariable=computer_score)
computer_score_display.place(x=220, y=65)

# Computer Choice Display
copm_choice = StringVar()
computer_choice_display = tk.Label(master=window, textvariable= copm_choice, font="Arial 20", bg="#121212", fg="Red")
computer_choice_display.pack(pady=5)

# Border between user and computer
who_won = StringVar()
computer_choice_display = tk.Label(master=window, height=1, width=100, textvariable= who_won, bg="Orange", font="Arial 30")
computer_choice_display.pack(pady=2)


# User Score Display
user_score = StringVar()
user_score.set("0")
user_score_display = tk.Label(master=window, bg="Green", height=1, width=5,
                                    font="Arial 15 bold", fg="White", textvariable=user_score)
user_score_display.place(x=220, y=170)

# User Choice Display
your_choice = StringVar()
user_choice_display = tk.Label(master=window, textvariable= your_choice, font="Arial 20", bg="#121212", fg="Green")
user_choice_display.pack()


# Create button for user
btn_frame =tk.Frame(master=window, bg="#121212")

rock_btn = tk.Button(master=btn_frame, text="Rock", bg= "#414040", fg="#ffffff",width=10, command= lambda :choice_winner("Rock"))
rock_btn.pack(side="left", padx=7)

paper_btn = tk.Button(master=btn_frame, text="Paper", bg= "#414040", fg="#ffffff",width=10, command= lambda :choice_winner("Paper"))
paper_btn.pack(side="left", padx=7)

scissor_btn = tk.Button(master=btn_frame, text="Scissor", bg= "#414040", fg="#ffffff",width=10, command= lambda :choice_winner("Scissor"))
scissor_btn.pack(side="left", padx=7)

btn_frame.pack(pady=20)

# Run
window.mainloop()