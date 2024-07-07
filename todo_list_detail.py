#to ask user numbers of todo and display the todo list
total_todo = int(input("Enter number of todos : "))
todos = []
#ask 
for i in range(0,total_todo):
    todo = input(f"Enter todo {i+1} : ")
    todos.append(todo)

#display
for todo in todos:
    print(todo) 