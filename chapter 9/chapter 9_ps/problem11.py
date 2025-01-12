with open("old.txt") as file:
    content = file.read()

with open("new.txt" , "w") as file:
    file.write(content)