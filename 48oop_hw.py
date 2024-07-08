#create a program to create a class Laptop[id,name,ram] and create 3 objects of it and print all details
class Laptop:
    def __init__(self,id,name,ram):
        self.id = id
        self.name = name
        self.ram = ram

    
    def display(self):
        print(f"Id : {self.id}\t Name : {self.name}\t Ram : {self.ram}\n")

#objects of class teacher
l1 = Laptop(id = 1234, name = "Dell", ram = "8Gb")
l2 = Laptop(id = 5678, name = "Acer", ram = "6Gb")
l3 = Laptop(id = 9101, name = "Lenovo", ram = "8Gb")

#display
l1.display()
l2.display()
l3.display()