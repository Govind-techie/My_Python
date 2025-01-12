word = "donkey"

with open("file.txt" , "r") as file:
   content = file.read()

content_new = content.replace("donkey","######")

with open("file.txt" , "w") as file:
   content = file.write(content_new)

   
