import tkinter as tk

def roi():
    investment = float(e_investment.get())
    income = float(e_income.get())
    profit = income - investment
    result = profit/investment*100
   #messagebox.showinfo("Result", f"The intrest is {result}")
    label_result = tk.Label(root,text = f"The ROI is : {result}%")
    label_result.pack()

root = tk.Tk()
root.title("ROI Calculator")
root.geometry("500x500")

#get investment
l_investment = tk.Label(root,text = "Enter Investment : ")
l_investment.pack()
e_investment = tk.Entry(root)
e_investment.pack()
#income
l_income = tk.Label(root,text = "Enter Income : ")
l_income.pack()
e_income = tk.Entry(root)
e_income.pack()

#button
button = tk.Button(root,text = "Calculate",command = roi,padx=50)
button.pack()

root.mainloop()