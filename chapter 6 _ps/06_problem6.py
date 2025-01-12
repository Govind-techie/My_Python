marks = int(input("enter your marks : "))

if(marks<=100 and marks>=90):
    print("you get an Excellent grade for marks" , (marks)) 

elif(marks<=90 and marks>=80):
    print("you get an A grade for marks", (marks))

elif(marks<=80 and marks>=70):
    print("you get a B for marks ", (marks))

elif(marks<=70 and marks>=60):
    print("you get a C for marks ", (marks))

elif(marks<=60 and marks>50):
    print("you get a D for marks ", (marks))

elif(marks<=50):
    print("you get a F grade and you fail for marks",(marks))


# Note : In this program we didnt use else instead we use an elif with such condition that it ends the program if the value goes below a certiain value
# Note : this if and elif statement ladder works independent without an else statement
