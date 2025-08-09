import tkinter as tk
from tkinter import font as tkFont

root = tk.Tk()

content = tk.Frame(root)
name = tk.Entry(content)

helv = tkFont.Font(family="Helvetica", size=100)

b1 = tk.StringVar()
b2 = tk.StringVar()
b3 = tk.StringVar()
b4 = tk.StringVar()
b5 = tk.StringVar()
b6 = tk.StringVar()
b7 = tk.StringVar()
b8 = tk.StringVar()
b9 = tk.StringVar()
current_player="X"

def checkwin():
    if b1 == b2 and b2 == b3:
        return 0
    elif b4 == b5 and b5 == b6:
        return 0
    elif b7 == b8 and b8 == b9:
        return 0
    elif b1 == b4 and b4 == b7:
        return 0
    elif b2 == b5 and b5 == b8:
        return 0
    elif b3 == b6 and b6 == b9:
        return 0
    elif b1 == b5 and b5 == b9:
        return 0
    elif b3 == b5 and b5 == b7:
        return 0
    return 1

def set_button(button):
    while checkwin() == 1:
        if button.get()=="":
            global current_player
            button.set(current_player)
            if current_player == "X":
                current_player = "O"
            elif current_player == "O":
                current_player = "X"
        else:
            print("Ungültiger Zug")

Button1 = tk.Button(content, textvariable=b1, width=2, command=lambda: set_button(b1), font=helv)
Button2 = tk.Button(content, textvariable=b2, width=2,command=lambda: set_button(b2), font=helv)
Button3 = tk.Button(content, textvariable=b3, width=2,command=lambda: set_button(b3), font=helv)
Button4 = tk.Button(content, textvariable=b4, width=2,command=lambda: set_button(b4), font=helv)
Button5 = tk.Button(content, textvariable=b5, width=2,command=lambda: set_button(b5), font=helv)
Button6 = tk.Button(content, textvariable=b6, width=2,command=lambda: set_button(b6), font=helv)
Button7 = tk.Button(content, textvariable=b7, width=2,command=lambda: set_button(b7), font=helv)
Button8 = tk.Button(content, textvariable=b8, width=2,command=lambda: set_button(b8), font=helv)
Button9 = tk.Button(content, textvariable=b9, width=2,command=lambda: set_button(b9), font=helv)


content.grid(column=0, row=0)
Button1.grid(column=0, row=0)
Button2.grid(column=1, row=0)
Button3.grid(column=2, row=0)
Button4.grid(column=0, row=1)
Button5.grid(column=1, row=1)
Button6.grid(column=2, row=1)
Button7.grid(column=0, row=2)
Button8.grid(column=1, row=2)
Button9.grid(column=2, row=2)

root.mainloop()