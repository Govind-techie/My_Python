# LENGTH FUNTION
name = "govind"
print(len(name)) # it gives the total length of string

# STARTSWITH FUNCTION
name = "govind"
print(name.startswith("go")) # it give a boolean value (true or false) 
print(name.startswith("ovind")) # eg. it see only for first value is present or not

# ENDSWITH FUNCTION
name = "govind"
print(name.endswith("ind")) # it give a boolean value (true or false) 
print(name.endswith("govin")) # eg. it only see for last value is present or not

# CAPTALIZE FUNCTION 
name = "govind"
print(name.capitalize()) # it makes a lower case letter into upper case letter (only valid for 1st letter of string)

a ="hello world"
print(a.lower()) # Output: "hello"

print(a.upper()) # Output: "HELLO"

print(a.title())  # Output: "Hello World"

b = " hello "
print(b.strip()) # Output: "hello"

print(b.lstrip())  # Output: "hello  "

print(b.rstrip())  # Output: "  hello"

print(a.replace("world", "there")) # Output: "hello there"

print(a.find("world"))  # Output: 6

c = "hello world world"
print(c.rfind("world"))  # Output: 12

print(a.split()) # Output: ["hello", "world"]

d = "-"
print(d.join(["2024", "09", "03"])) # Output: "2024-09-03"

e = "hello , {}!"
print(e.format("Alice")) # Output: "Hello, Alice!"

name2 = "Alice"
print(f"Hello, {name2}!")  # Output: "Hello, Alice!"

f = "hello"
print((f).isalpha())  # Output: 

g = "123"
print((g).isdigit())  # Output: True

h = "  "
print((h).isspace())  # Output: True



