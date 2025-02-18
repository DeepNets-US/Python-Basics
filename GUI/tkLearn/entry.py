import tkinter as tk

# Main window
win = tk.Tk()

# Create widgets
ask_name = tk.Label(text='What is your name?')
user_in = tk.Entry(fg='blue', bg='yellow', width=50)

print(f'So your name is {user_in.get()}')

# Pack all & run
ask_name.pack()
user_in.pack()
win.mainloop()
