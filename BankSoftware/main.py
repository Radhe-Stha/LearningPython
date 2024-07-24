from customer import Customer
import controller as c
import csv 

option_text = """
What do you want to do[1-5]
1. Add new Customer
2. View Customer
3. View Customer by Id
4. Update Customer
5. Delete Customer
"""
option = int(input(option_text))

if option == 1:
    c.add_customer()
elif option == 2:
    c.view_customer()
elif option == 3:
    print("View customer by id ")
    c.view_singlecustomer()
elif option == 4:
    print("Update Customer")
elif option == 5:
    print("Delete customer")
    c.delete_customer()
else :
    print("Invalid option !")