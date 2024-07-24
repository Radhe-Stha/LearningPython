from main import create_connection

con = create_connection()
cursor = con.cursor()
id = input("Enter id to update : ")
name = input("Enter name : ")
phone = input("Enter phone : ")
cursor.execute(f"UPDATE contacts SET name = '{name}',phone = '{phone}' WHERE id = {id}")
con.commit()
print("Record updated successfully.")
con.close()