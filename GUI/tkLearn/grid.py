import tkinter as tk

win = tk.Tk()

for i in range(3):
    for j in range(3):
        frame = tk.Frame(master=win, borderwidth=1, relief=tk.RAISED)
        frame.grid(row=i, column=j)

        lbl = tk.Label(text=f'Row {i}\nColumn {j}', master=frame)
        lbl.pack(padx=50, pady=50)

win.mainloop()
