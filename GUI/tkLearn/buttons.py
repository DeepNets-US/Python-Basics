import tkinter as tk

win = tk.Tk()
button = tk.Button(
    text='Click Me!',
    fg='red',
    bg='orange',
    width=10,
    height=10
)
button.pack()
win.mainloop()
