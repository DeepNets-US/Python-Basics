import tkinter as tk

win = tk.Tk()
win.rowconfigure(0, minsize=50, weight=1)
win.columnconfigure([0, 1, 2], minsize=50, weight=1)

lbl = tk.Label(text='0')

def inc():
    lbl['text'] = f'{int(lbl['text']) + 1}'

def dec():
    lbl['text'] = f'{int(lbl['text']) - 1}'

btn1 = tk.Button(text='+', command=inc)
btn2 = tk.Button(text='-', command=dec)

btn1.grid(row=0, column=0, sticky='nsew')
lbl.grid(row=0, column=1)
btn2.grid(row=0, column=2, sticky='nsew')

win.mainloop()
