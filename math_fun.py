#create function that find square of number
import math
def square(num):
    num = num * num
    print(num)


square(4)


number = 3.13434544
print(f"num is : {number:.3f}")
print(f"num is : {number:.2f}")

print(math.ceil(10.1))
print(math.floor(10.3))

def round_number(n):
    round_number = round(n)
    print(round_number)

user_input = float(input("Enter number : "))
round_number(user_input)
