# it imports the os module
import os
# it shows the path of directory, you can change according to your requirement
def print_directory_contents(path):
    with os.scandir(path) as entries:
        for entry in entries:
            print(entry.name)

print_directory_contents('.')

# this program print directory using os module 
# problem4 ends
