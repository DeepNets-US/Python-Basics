import tkinter as tk

win = tk.Tk()

btn = tk.Button(text='Click Me!')
btn.bind('<Button-1>', lambda x: print('Button Clicked!'))
btn.pack()

win.mainloop()
