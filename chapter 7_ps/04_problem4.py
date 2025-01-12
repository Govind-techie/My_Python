n = int(input("enter a no. : "))

for i in range(2,n):
    if(n%i == 0):
        print("The given no. is not a prime no.",(n))
        break
else:
    print("The given no. is a prime no.",(n))