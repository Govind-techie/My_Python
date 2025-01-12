# Join Method : Join methof joins a list of string with a particular character and convert it into and entire string instead of list.

# Example :

Fullname = ["Govind","Shesharam","Choudhary"]

print(" ".join(Fullname)) # Here, it adds the space (" ") between each string element of list and prints it as an entire string.
print(",".join(Fullname)) # Here, it adds the comma (,) between each string element of list and prints it as an entire string.

num = [1,2]
# print(",".join(num)) # It will return an error, because only list of strings can be joined. Join method can't be used with list of numbers.
