import tkinter as tk

win = tk.Tk()

def handle_keypress(event):
    print(event.char)

win.bind('<Key>', handle_keypress)

win.mainloop()
