import tkinter as tk
from tkinter import messagebox

def simple_interest():
    p = float(entry_p.get())
    t = float(entry_t.get())
    r = float(entry_r.get())
    result = p*t*r/100
   #messagebox.showinfo("Result", f"The intrest is {result}")
    label_result = tk.Label(root,text = f"The Intrest is : {result}")
    label_result.pack()

root = tk.Tk()
root.title("Simple Interest Calculator")
root.geometry("500x500")

#principle
label_p = tk.Label(root,text = "Enter Principla : ")
label_p.pack()
entry_p = tk.Entry(root)
entry_p.pack()
#time
label_t = tk.Label(root,text = "Enter Time : ")
label_t.pack()
entry_t = tk.Entry(root)
entry_t.pack()
#rate
label_r = tk.Label(root,text = "Enter Interest rate : ")
label_r.pack()
entry_r = tk.Entry(root)
entry_r.pack()

#button
button = tk.Button(root,text = "Calculate",command = simple_interest,padx=50)
button.pack()

root.mainloop()