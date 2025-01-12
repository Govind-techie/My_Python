# Global : Global keyword is used to change the value of global value with the local value belongs to that particular function.

# Note : Global keyword is always used with a function to change the global value to local value of that functions.

a = 4 # It is a global value 

def global_change():
    global a # It will change the value of global (a) with the local (a) belongs to that particular function.
    a = 3 # It is a local value of belongs to a function.
    print(a)


global_change()

print(a) # It will print the changed global(a).