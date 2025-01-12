def generatetable(n):
    table = ""
    for i in range (1,11):
        table += f"{i} x {n} = {i*n}\n"

    with open(f"table/table_{n}" , "w") as file:
        file.write(table)


for i in range (2,21):
    generatetable(i)
