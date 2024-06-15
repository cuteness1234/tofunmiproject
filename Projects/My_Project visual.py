import tkinter as tk

master = tk.Tk()
label_str = tk.StringVar()
tk.Label(master, textvariable=label_str).grid(row=0)
label_str.set("Type a number from 0-100")

el = tk.Entry(master)

def read_number ():
    label_str.set(f"You tried {el.get()}")

el.grid(row=1, column=0)
tk.Button(master,
          text='Show', command=read_number).grid(row=2,
                                                 column=0,
                                                 sticky=tk.W,
                                                 pady=4)

master.mainloop()
