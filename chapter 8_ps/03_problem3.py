# 3. How do you prevent a python print() function to print a new line at the end.

def prevent_line():
    print("a")
    print("b")
    print("c",end="")
    print("d",end="")

prevent_line()