import tkinter as tk

win = tk.Tk()
msg = tk.Label(
    text='This is a text message.',
    foreground='blue',
    background='orange',
    width=100,
    height=20
)
msg.pack()
win.mainloop()
