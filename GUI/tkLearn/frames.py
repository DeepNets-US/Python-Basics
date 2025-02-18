import tkinter as tk

win = tk.Tk()

# Elements of frame 1
f1 = tk.Frame(width=1000, height=50, bg='green')
lbl = tk.Label(
    master=f1,
    text='This is frame A'
)
lbl.pack()
f1.pack()

# Add another frame
f2 = tk.Frame(width=50, height=25, bg='orange')
lbl = tk.Label(master=f2, text='This is frame B', fg='blue')
lbl.pack()
f2.pack()

# Final Loops
win.mainloop()
