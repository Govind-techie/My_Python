file = open("poems.txt")
content = file.read()
if ("twinkle" in content):
    print("The given file contains the word twinkle")
else:
    print("The given file does not contain the word twinkle")
print(content)
file.close()
