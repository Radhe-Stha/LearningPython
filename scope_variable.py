#reverse string
def reverse_string(text):
    name = text
    reverse_string = ""
    for i in range(len(name)- 1, -1,-1):
        reverse_string = reverse_string + name[i]
    print(f"Reverse string is : {reverse_string}")
        


reverse_string("radha")