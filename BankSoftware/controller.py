from customer import Customer
import csv
import controller as c

all_customers= []

# Convert customers to csv
def convert_customer_to_csv(listofcustomer):
    file = open("customers.csv", "w")
    file.write("")
    file.close()
    for c in listofcustomer:
        f = open("customers.csv", "a")
        f.write(f"{c.id},{c.name},{c.balance},{c.citizenship},{c.phone}\n")
        f.close()

# Convert csv to customer list
def convert_csv_to_customer_list():
    all_customers = []
    with open('customers.csv', 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            c = Customer(id=row[0], name=row[1], phone=row[4], balance=float(row[2]), citizenship=row[3])
            all_customers.append(c)
    return all_customers


def add_customer():
    print("Adding Customer")
    c = Customer(id = "", name = "", phone = "", balance = 0, citizenship = "")
    c.id = input("Enter Customer Id : ")
    c.name = input("Enter Customer Name : ")
    c.phone = input("Enter Customer Phone Number : ")
    c.balance = float(input("Enter Customer Balance : "))
    c.citizenship =input("Enter Customer Citizenship Number : ")

    f = open("customers.csv", "a")
    f.write(f"{c.id},{c.name},{c.phone},{c.balance},{c.citizenship}\n")
    f.close()
    print(f"Customer {c.name} added successfully")

def view_customer():
    f = open("customers.csv","r")
    print(f.read())

def view_singlecustomer():
    print("View Single Customer by Id")
    id = input("Enter Customer Id : ")
    with open("customers.csv","r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:  #print(f"{row} Hello)
            c = Customer(id = row[0],name = row[1], phone = row[2], balance = float(row[3]), citizenship = row[4])
            all_customers.append(c)

    record_found = False
    customer = Customer(id="",name="",phone="",balance=0,citizenship="")
    for c in all_customers:
        if c.id == id:
            record_found = True
            customer = c
            break
        else:
            record_found = False
    if record_found == True:
        print("Record is found : ")
        customer.display_customer()
    else: print("Customer is not found.") 
           

def update_customer():
    print("Updating Customer")

def delete_customer():
    print("Delete Customer")
    lists = c.convert_csv_to_customer_list()
    updated_customer = []
    idtodelete= input("Enter customer id: ")
    record_found = False
    for customer in lists:
        if customer.id == idtodelete:
            record_found = True
        else:
            updated_customer.append(customer)

    if record_found:
        c.convert_customer_to_csv(updated_customer)
        print("Deleted Successfully")
    else:
        print("No record found")

def update_customer(id):
    print(f"Updating customer id {id}")
    
def search_customer(first_name):
    print("Searching customer")