def func():
    print("hello world")

# Here, it checks whether the code is executed from the main file or some different file.
# If the code is executed from the main file it will excute the code.
# If the code is executed from a different file it will not execute the code

if __name__ == "__main__":
    print(f"This code is directly executed from the {__name__} file")
    func()
else:
    print(f"It is executed from a different file named as {__name__}, code cannot be run")
    