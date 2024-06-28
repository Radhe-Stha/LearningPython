#

"""# create multiplication table of 9
for i in range(1,11):
    print(f"9 * {i} = {9*i}")
start = int(input("Enter start number : "))
end = int(input("Enter end number : "))

for i in range(start,end + 1):
    for j in range(1,11):
        print(f"{i} * {j} = {i*j}")
    print("\n-----\n")"""

"""#ask user to enter n nos of fruit and enter fruit name and print that list
fruits =[]
total_fruit = int(input("Enter total number of fruits : "))
for i in range(1,total_fruit + 1):
    fruit = input(f"Fruit {i} =  ")
    fruits.append(fruit)

print("\n-----\n")
print("All fruits are :")
for fruit in fruits:
    print(fruit)"""
#atm 
atm_pin = '1456'
user_pin = ''
attempt = 0
while atm_pin != user_pin:
    if attempt >0:
        print(f"Invalid pin code. total attempt {attempt}")
    user_pin = input("Enter atm pin : ")
    attempt = attempt + 1
print("access granted, Enter amount : ")
