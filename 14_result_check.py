#create a program that tests result of student , taking symbol no from user

resultset = {
    "aa11": "3",
    "ab12": "2",
    "ac13": "3.5",
    "ad14": "4",
    "ae15": "3",
    "af16": "2.5"
}
symbol_no = input("Enter Symbol Number : ")
result = ""
for i in resultset.keys():
    #print(i)
    if symbol_no == i:
        result = resultset[i]
        break
    else:
        result = ""
if result != "":
    print(f"Your result is {result}")
else:
    print("Symbol Number not found !")

