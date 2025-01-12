# Multiple Context Manager : The multiple context manager allows to handle to manage many resources within a single with statement.

with open("file1.txt") as f1, open("file2.txt") as f2:
    # Your code goes here
    content1 = f1.read()
    content2 = f2.read()

    print("Content of file1:", content1)
    print("Content of file2:", content2)