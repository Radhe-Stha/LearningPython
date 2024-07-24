import tkinter as tk

def add_customer():
    pass
def view_customer():
    pass
def single_view():
    pass
def delete_customer():
    pass
def update_customer():
    pass
root = tk.Tk()
root.title("GUI")
root.geometry("500x500")

label_topic = tk.Label(root,text = "Welcome to our Bank Software").pack()
label_customer = tk.Label(root,text = "Customer").pack()
button_add = tk.Button(root,text = "Add customer",command = add_customer,padx = "60").pack()
button_view = tk.Button(root,text = "View all Customer",command = add_customer,padx = "60").pack()
button_singleview = tk.Button(root,text = "View Single Customer",command = single_view,padx = "60").pack()
button_delete = tk.Button(root,text = "Delete Customer",command = delete_customer,padx = "60").pack()
button_update = tk.Button(root,text = "Update Customer",command = update_customer,padx = "60").pack()

root.mainloop()