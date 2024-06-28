"""#Display person age from his/her birth year

birth_year = int(input("Enter your birth year : "))
age = 2024 - birth_year

print(f"Your age is {age}")

if age >= 18:
    print("You are a voter.")
else :
    print("You are not a voter.")"""

"""#Ask user to enter a price, if price is greater than 500, it is expensive other wise it is ok
price = float(input("Enter price : "))
if price >= 500:
    print("The price is expensive.")
else:
    print("The price is Ok.")"""

"""#Ask user to enter a number and find that number is odd or even
num = int(input("Enter num : "))
if num %2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")"""

#greater number
n1 = 100
n2 = 100
n3 = 100

if n1 > n2 and n1 > n3:
    print(f"{n1} is greater")
elif n2 > n1 and n2 > n3:
    print(f"{n2} is greater")
elif n3 > n1 and n3 > n2:
    print(f"{n3} is greater")
else:
    print("something is wrong")
