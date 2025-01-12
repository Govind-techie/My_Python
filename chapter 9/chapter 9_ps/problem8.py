with open("this.txt") as file:
    content = file.read()

with open("copy this.txt" , "w") as file:
    file.write(content)

