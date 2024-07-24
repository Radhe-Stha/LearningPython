from main import create_connection

con = create_connection()
cursor = con.cursor()
name = input("Enter name : ")
phone = input("Enter phone : ")
cursor.execute("INSERT INTO contacts (name,phone) VALUES (%s, %s)",(name, phone))
con.commit()
con.close()
print("Insert data successfull")
