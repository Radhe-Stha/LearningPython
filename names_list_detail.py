#ask user to enter n names of people names
#and print all names that starts with B
#if there is no name, it should say "No name found"
#and in there is/are names , it should display all names

total_names = int(input("Enter number of names : "))
names = []
#ask names from user
for i in range(0,total_names):
    name = input(f"Enter name {i+1} : ")
    names.append(name)

#display names with B

#names_with_b = [name for name in names if name[0].lower() == 'b']
#print(names_with_b)

names_with_b = []
for name in names:
     if name[0].lower() == 'b':
         names_with_b.append(name)
     else:
        continue

if names_with_b == []:
    print("No name found starting with 'B'!")
else:
    print(names_with_b)