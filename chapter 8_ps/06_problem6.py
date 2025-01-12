# 6. Write a python function which converts inches to cms.

# cm = inches x 2.54
# therefore,
# inches = cm/2.54

def inches(cm):
    return cm/2.54

cm = int(input("Enter your length in cm : "))

print(inches(cm))