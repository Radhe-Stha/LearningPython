try:
    dob = int(input("Enter birth year  :"))
    age = 2024 - dob
    print(f"Age is {age}")
except:
   print("Please enter numeric value only")
finally:
    print("end")


