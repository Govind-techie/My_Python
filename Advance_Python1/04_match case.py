# Match Case : In match case we give a ceratin case and if it match with a particular gaiven value it returns the case value.

# Example :

def numbers(number : int ) -> int: # Here, we define a function numbers with a parameter as number.
    match number: # It matches the number with each case if the number matches to a particular case it returns the case value.
        case 100: # Here case_1 
            return f"The number is {number}"
        case 200: # Here case_2
            return f"The number is {number}"
        case 300: # Here case_3
            return f"The number is {number}"
        case _: # Here case_4
            return f"Invalid number"
        
print(numbers(100))

# Note : In case_4 we mention a underscore (_) symbol represent that any input will match to that case and return the value of that case.
        