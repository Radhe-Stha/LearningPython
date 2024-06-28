#add your electricity bill from jan to dec in dictionary and find total and average bill amount
print("Month    Electricity Bill(Rs.)")
electricity_bill = {
    'Jan': 2000,
    'Feb': 2200,
    'Mar': 2300,
    'Apr': 1900,
    'May': 1800,
    'Jun': 1700,
    'Jul': 1500,
    'Aug': 1600,
    'Sep': 1800,
    'Oct': 1900,
    'Nov': 2000,
    'Dec': 2100
}
for k, v in electricity_bill.items():
    print(k,v)
    
total = sum(electricity_bill.values())
print(f"Total amount of Electricity Bill of the year 2023 is : {total}")
print(f"Average amount of Electricity Bill of the year 2023 is :{total/12}")

    