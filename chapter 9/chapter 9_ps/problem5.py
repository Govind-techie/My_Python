words = ["donkey" , "ganda " , "bad"]

with open("file.txt" , "r") as file:
   content = file.read()
for word in words:
 content = content.replace(word , "*" * len(word))

with open("file.txt" , "w") as file:
   content = file.write(content)