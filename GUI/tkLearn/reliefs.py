import tkinter as tk

# Main window
win = tk.Tk()


# Widgets
f1 = tk.Frame(relief=tk.FLAT, borderwidth=10)
label = tk.Label(text='Flat', width=20, height=10, master=f1, relief=tk.FLAT)
label.pack()

f2 = tk.Frame(relief=tk.SUNKEN, borderwidth=10)
label = tk.Label(text='Sunken', width=20, height=10, master=f2, relief=tk.SUNKEN)
label.pack()

f3 = tk.Frame(relief=tk.RAISED, borderwidth=10)
label = tk.Label(text='Faised', width=20, height=10, master=f3, relief=tk.RAISED)
label.pack()

f4 = tk.Frame(relief=tk.GROOVE, borderwidth=10)
label = tk.Label(text='Groove', width=20, height=10, master=f4, relief=tk.GROOVE)
label.pack()

f5 = tk.Frame(relief=tk.RIDGE, borderwidth=10)
label = tk.Label(text='RIdge', width=20, height=10, master=f5, relief=tk.RIDGE)
label.pack()


# Pack All frames
f1.pack(side=tk.LEFT)
f2.pack(side=tk.LEFT)
f3.pack(side=tk.LEFT)
f4.pack(side=tk.LEFT)
f5.pack(side=tk.LEFT)


# Application Packing
win.mainloop()
