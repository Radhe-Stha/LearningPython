import requests
import json
from tkinter import*
import tkinter as tk

def display_quotes():
    pass
    


root = tk.Tk()
root.title("JSON Quotes")
#label
l_url = tk.Label(root,text = "Url : ").pack()
#ask url
e_url = tk.Entry(root).pack()

#button 
btn_quotes = tk.Button(root,text = "Quotes",command = display_quotes).pack()
l1 = tk.Label(root,text = "Quotes").pack()

f = requests.get(e_url)
text = f.text
obj = json.loads(text)
print(obj["text"])

root.mainloop()

