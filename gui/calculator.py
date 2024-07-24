import tkinter as tk
from tkinter import messagebox

def get_sum():
    #get value from textbox
    value1 = float(entry1.get())
    value2 = float(entry2.get())
    sum = value1 + value2
    diff = value1- value2
    messagebox.showinfo("Result", f"The sum is {sum}\n The diff is {diff}")


def hello():
    entry1.setvar("Hello")


root = tk.Tk()
root.title("Calculator")
root.geometry("300x500")
root.config(bg="")

#first num
label1 = tk.Label(root, text = "Enter first number : ")
label1.pack(padx=5)
#label1.grid(row=0,column=0)
entry1 = tk.Entry(root)
entry1.pack(padx=5)

#second num
label2 = tk.Label(root, text = "Enter second number : ")
label2.pack(padx=5)
#label2.grid(row=1,column=0)
entry2 = tk.Entry(root)
entry2.pack(padx=5)

#result
label3 = tk.Label(root, text = "Result")
label3.pack(padx=5)
#label2.grid(row=1,column=0)
entry3 = tk.Entry(root)
entry3.pack(padx=5)

#button
button1 = tk.Button(root, text = "Calculate", command = hello)
button1.pack(padx=5)


#run loop
root.mainloop()