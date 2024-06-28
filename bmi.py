#calculate BMI using given height and weight

ht = float(input("Enter height in meter : "))
wt = float(input("Enter weight in kg : "))

bmi = wt/(ht**2)

print(f"Your Body Mass Index is : {bmi:.2f}")
if bmi < 18.5:
    print("You are Underweight")
elif bmi < 25:
    print("You are Normal")
elif bmi < 30:
    print("You are Overweight")
else:
    print("You are Obese")