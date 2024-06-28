#program to convert given nepali rupee to us doller ,japanese yen, european euro,
rs = float(input("Enter Nepali amount in Rs. : "))
us  = rs/133.36
euro = rs/142.51
yen = rs*1.2

print(f"Nepali Rs. {rs} = $ {us:.2f} Us Dollars")   #:.2f prints only 2 digits after decimal
print(f"Nepali Rs. {rs} = ¢ {euro:.2f} European Euro")
print(f"Nepali Rs. {rs} = ¥ {yen:.2f} Japanese Yen")

# Conversion rates
npr_to_usd = 133.69
npr_to_euro = 142.96
npr_to_yen = 0.84

# User input
user_input = input("Enter amount in Nepali Rupees (NPR): ")

# Convert user input to float
amount_npr = float(user_input)

# Calculate the conversions
amount_usd = amount_npr / npr_to_usd
amount_euro = amount_npr / npr_to_euro
amount_yen = amount_npr * npr_to_yen

# Print the results
print(f"The amount in USD is: ${amount_usd:.2f}")
print(f"The amount in Euro is: €{amount_euro:.2f}")
print(f"The amount in Japanese Yen is: ¥{amount_yen:.2f}")