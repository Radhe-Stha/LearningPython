#create 10 employees who work on diffrernt department 
# print all employee who are in IT department
# optional : display all department along with their details
names = [
    # name, department
    ("Sagar Aryal", "Microbiology"),
    ("Santosh Adhikari", "IT"),
    ("Subin Thapa", "IT"),
    ("Mandip Hirachan", "IT"),
    ("Sujan Khadka", "Finance"),
    ("Samyak Pokharel", "MBA"),
    ("Binod Rayamajhee", "Microbiology")
]

### Find All From Microbiology Department
microbiology_names = [name for name in names if name[1] == "Microbiology"]

for i in microbiology_names:
    print(i[0])
