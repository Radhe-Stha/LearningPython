import json
import requests
import tkinter as tk

def func():
    #url = e.get()
    #x=1
    names = ['a','b','c','d']
    num = [1,2,3,4]
    l2 = tk.Label(root,text=f"{num}.{names}").place(x=20,y=130)
    
           

root = tk.Tk()
root.title("api_Gui")
root.geometry("800x800")

#get url
l = tk.Label(root,text = "Url : ").place(x=10,y=10)
e = tk.Entry(root,width="50").place(x=50,y=10)

#button
btn = tk.Button(root,text="Scrap",command=func).place(x=50,y=50)
l1 = tk.Label(root,text="Display").place(x=20,y=80)

root.mainloop()