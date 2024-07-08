class Teacher:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary


    def display(self):
        print(f"Name : {self.name} \t Salary : {self.salary}\n")
        

#object of class teacher
t1 = Teacher(name = "Ram", salary = 30000)
t2 = Teacher(name = "Hari", salary = 35000)
t3 = Teacher(name = "Sita", salary = 35000)


t1.display()
t2.display()
t3.display()