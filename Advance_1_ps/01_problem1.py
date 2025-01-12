# 1. Write a program to open three files 1.txt, 2.txt and 3.txt if any these files are not
# present, a message without exiting the program must be printed prompting the same.

files = ["1.txt","2.txt","3.txt"] # Here, we created a list of files

for file_name in files: # We iterate through each files present in the list  of files
    try: # Here, we created a try block if the code execute without an error
        with open( file_name , "r") as file: # We, are opening each file with context manager each time it iterates over the files
            print(f"The content of {file_name} is {file.read()}") # if the file is pressent it will read the content of that file
    except FileNotFoundError: # It will raise an exception
        print(f"File not found {file_name}!!") # Here, if the file is not found instead of error it will print this.

        

    