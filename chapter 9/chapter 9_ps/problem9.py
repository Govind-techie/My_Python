with open("this.txt") as file:
    content = file.read()

with open("copy this.txt") as file:
    content2 = file.read()

if (content in content2):
    print("The content in both the file is identical")
else:
    print("The content in both the file is not identical")