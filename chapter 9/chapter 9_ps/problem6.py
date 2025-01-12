with open("log.txt") as file:
    content = file.read()

    if ("python" in content):
        print("yes python is present")
    else:
        print("python is not present")