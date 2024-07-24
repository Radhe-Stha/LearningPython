from product import Product

option_text = """""
what do you want to do [1-2]
1. Add product
2. View all prodiucts
"""
option = int(input(option_text))
if option == 1:
    p = Product(id = 0, name = "", qty = 0, price = 0)
    p.id = int(input(f"Enter product {i+1} id : "))
    p.name = (input(f"Enter product {i+1} name : "))
    p.qty = int(input(f"Enter product {i+1} quantity : "))
    p.price = float(input(f"Enter product {i+1} price : "))

    f = open('product.csv', 'a')
    f.write(f"{p.id},{p.name},{p.qty},{p.price}")
    f.close()
    print("Product added successfully")
elif option == 2:
    f = open("product.csv", 'r')
    
total_product = int(input("No. of products : "))
for i in range(total_product):
    p = Product(id = 0, name = "", qty = 0, price = 0)
    p.id = int(input(f"Enter product {i+1} id : "))
    p.name = (input(f"Enter product {i+1} name : "))
    p.qty = int(input(f"Enter product {i+1} quantity : "))
    p.price = float(input(f"Enter product {i+1} price : "))

    f = open('product.csv', 'a')
    f.write(f"{p.id},{p.name},{p.qty},{p.price}")
    f.close()

print("Saved")