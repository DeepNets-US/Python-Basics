import tkinter as tk

win = tk.Tk()

widths = [500,400,300]
heights = [300, 200, 100]
colors = ['pink', 'green', 'yellow']

for (height, width, color) in zip(heights, widths, colors):
    f = tk.Frame(master=win, bg=color, height=height, width=width)
    f.pack(fill=tk.X, side=tk.RIGHT)

win.mainloop()
