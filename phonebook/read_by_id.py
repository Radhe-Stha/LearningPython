from main import create_connection

con = create_connection()
cursor = con.cursor()
id = input("Enter id : ")
cursor.execute(f"SELECT * FROM contacts WHERE ID = {id}")
contacts = cursor.fetchall()
for i in contacts:
    print(i)
con.close()