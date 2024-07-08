#Create a list of 10 employees, each belonging to a different department,
# and print the details of all employees who are in the IT department.

employee = [
    #names  , Department  , Address , Age
    ("Ram", "IT", "Kathmandu", "25"),
    ("Shyam", "Managment", "Pokhara", "28"),
    ("Hari", "Acounting", "Dharan", "26"),
    ("Sita", "Nursing", "Jhapa", "24"),
    ("Geeta", "Medical", "Bhaktapur", "30"),
    ("Gopal", "IT", "Lalitpur", "28"),
    ("Amar", "it", "Kathmandu", "30"),
    ("Preeti", "Finance", "Banepa", "27"),
    ("Aakash", "IT", "Chitwan", "28"),
    ("Binod", "IT", "Itahari", "30")
]

#finding all employee from IT department

names_it = [names for names in employee if names[1].upper() == "IT"]

for i in names_it:
    print(i[0], i[1], i[2], i[3])
