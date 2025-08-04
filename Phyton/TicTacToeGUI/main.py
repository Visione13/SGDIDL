import tkinter as tk

root = tk.Tk()

content = tk.Frame(root)
name = tk.Entry(content)

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

def set_button(button):
    if button.get()=="":
        global current_player
        button.set(current_player)
        if current_player == "X":
            current_player = "O"
        elif current_player == "O":
            current_player = "X"
    else:
        print("Ungültiger Zug")

Button1 = tk.Button(content, textvariable=b1, width=10, height=5, command=lambda: set_button(b1))
Button2 = tk.Button(content, textvariable=b2, width=10, height=5, command=lambda: set_button(b2))
Button3 = tk.Button(content, textvariable=b3, width=10, height=5, command=lambda: set_button(b3))
Button4 = tk.Button(content, textvariable=b4, width=10, height=5, command=lambda: set_button(b4))
Button5 = tk.Button(content, textvariable=b5, width=10, height=5, command=lambda: set_button(b5))
Button6 = tk.Button(content, textvariable=b6, width=10, height=5, command=lambda: set_button(b6))
Button7 = tk.Button(content, textvariable=b7, width=10, height=5, command=lambda: set_button(b7))
Button8 = tk.Button(content, textvariable=b8, width=10, height=5, command=lambda: set_button(b8))
Button9 = tk.Button(content, textvariable=b9, width=10, height=5, command=lambda: set_button(b9))


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