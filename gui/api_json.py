import json
import requests
import tkinter as tk
#url = "https://jsonguide.technologychannel.org/quotes.json"
#f = requests.get(url)
#quotes = json.loads(f.text)
#for quote in quotes:
#    print(quote['text'])

def roi():
    url = e_url.get()
    f = requests.get(url)
    quotes = json.loads(f.text)
    for quote in quotes:
        l_display = tk.Label(root,text = f"{quote['text']}")
        l_display.pack()

root = tk.Tk()
root.title("Api json")
root.geometry("500x500")

#get url
l_url = tk.Label(root,text = "Url : ")
l_url.pack()
e_url = tk.Entry(root,width="70")
e_url.pack()


#button
button = tk.Button(root,text = "Scrap",command = roi,padx=50)
button.pack()

root.mainloop()