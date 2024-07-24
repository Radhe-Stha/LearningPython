
import tkinter as tk
from tkinter import messagebox

root = tk.Tk() 
root.title("btn")
def func():
    x = e_name.get()
    messagebox.showinfo(x)


l_name = tk.Label(root,text = "Name").pack()
e_name = tk.Entry(root).pack()

btn_submit = tk.Button(root,text = "Submit",command = func).pack()

l_text = tk.Label(root,text = "None",bg="blue").pack()

root.mainloop()


