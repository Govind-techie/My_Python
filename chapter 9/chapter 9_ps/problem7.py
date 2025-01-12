with open("log.txt") as file:
    lines = file.readlines()
    line_no = 1
for line in lines:
    if ("python" in line):
        print(f"yes python is present , line no. : {line_no}")
        break
    line_no += 1
    
else:
    print("python is not present")