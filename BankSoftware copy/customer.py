class Customer:
    def __init__(self,id,name,balance,phone,citizenship):
        self.id = id
        self.name = name
        self.balance = balance
        self.phone = phone
        self.citizenship = citizenship

    
    def display_customer(self):
        print(f"Customer name :{self.name}")
        print(f"Id : {self.id}")
       # print(f"Customer Name : {self.name}")
        print(f"Balance : {self.balance}")
        print(f"Phone Number : {self.phone}")
        print(f"Citizenship Number : {self.citizenship}")

        
