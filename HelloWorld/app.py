#input
#convert weight in pound to kg
'''
wt_lb = input('Your weight in pounds = ')
wt_kg = int(wt_lb) * 0.453
print(str(wt_kg) + ' kg')
'''


#formatted string
#print john [smith] is a coder
'''
first = 'John'
last = 'Smith'
message = first +' [' + last + '] ' 'is a coder'
msg = f'{first} [{last}] is a coder'
print(msg)
print(message)
'''

#LENgTH OF STRING
'''
name = 'My name is John'
print(len(name))

#methods of string

print(name.upper())
print(name.lower())
'''

#if ,elif , else statement
#house price 1 millon, if good credit 10 % down payment ,else 20%
'''
house_price = 1000000
is_goodcredit = True
if(is_goodcredit):
    down_payment = 0.1*house_price
else:
    down_payment = 0.2*house_price

print(f'Down Payment = ${down_payment}')
'''

#operator, and , or ,not
#if person has high income and good credit then only eligible for loan
'''
high_income = False
good_credit = False

if high_income and good_credit:
    print('Eligible for Loan.')
else :
    print('Not eligible for loan')
if high_income or good_credit:
    print('Eligible for loan')
else:
    print('Not eligible')
'''
#weight conveter in lbs and kg
'''
weight = int(input("Enter your weight : "))
unit = input("(L) for pounds and (k) for kg : ")
if unit.upper() == "L":
    converted = weight*0.453
    print(f'{converted} kg')
else:
    converted = weight/0.453
    print(f"{converted} lbs")
'''
#loops
#while
#Game : guess a secret number ,3 chances ,
'''secret_number = 9
guess_limit = 3
guess_count = 0
while guess_count < guess_limit:
    guess = int(input("Guess number : "))
    guess_count +=1
    if guess == secret_number:
        print("You WON !")
        break
else:
    print('You LOSE')'''
# Car game
"""command = ''
started = False 
while True:
    command = input('> ').lower()
    if command == 'help':
        print('''
start - to start the car
stop - to stop the car
quit - to exit the game''')
    elif command == 'start':
        if started:
            print('car already started')
        else:
            started = True
            print('car started')
    elif command == 'stop':
        if not started:
            print('car already stopped')
        else:
            started = False
            print('car stopped')
    elif command == 'quit':
        break
    else:
        print('Enter Valid Command')
"""
#for loop
"""for item in 'python':
    print(item)
for item in ['john', 'mosh', 'tom']:
    print(item)
for item in [1,2,3,4,5]:
    print(item)

price = [10,20,30]
total = 0
for item in price:
    total += item
print(f'total price = {total}')
"""
#Nested for loop
"""
for x in range(4):
    for y in range(2):
        print(f'{x} , {y}')
        """
# print the f letter patter with x using nested for loop
'''num = [5, 2, 5, 2, 2]
for item in num:
    for letter in 
    '''
#dictioanary
#key - value
#keys should be unique
#values can be changed
#keys and values can be added later in code also
'''
customer = {
    "name": "john",
    "age": 30,
    "is_married": True
}
print(customer)
print(customer.get("name"))
print(customer["name"])
#can add new key and value
print(customer.get("location","bhaktapur"))
# can change values of key
customer["name"] = "radhe"
print(customer.get("name"))

# number to words
#
"""numbers = {         #creating a diactionary
    "1": "One",     #key and value
    '2': 'Two',
    '3': "Three",
    '4': "Four",
    '5': "Five",
    '6': "Six",
    '7': "Seven",
    '8': "Eight",
    '9': "Nine",
    '0': "Zero",
    
}
words = input("Enter Numbers : ")
output = ""
for ch in words:
    output += numbers.get(ch) + " "
print(output)
"""
'''
# for emoji's cntrl + command + space in mac
def emoji_converter(message):
    words = message.split(" ")
    emojis = {
        ":)": "😀",
        ":(": "☹️"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input("> ")
print(emoji_converter(message))










