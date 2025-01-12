a = int(input("enter your no. 1 : "))
b = int(input("enter your no. 2 : "))
c = int(input("enter your no. 3 : "))
d = int(input("enter your no. 4 : "))

if (a>b and a>c and a>d): 
    print("The greatest no. is : " , (a))

elif(b>a and b>c and b>d):
    print("The greatest no. is : " , (b))

elif(c>a and c>b and c>d):
    print("The greates no. is : " , (c))

else :
    print("The greatest no. is : " , (d))
