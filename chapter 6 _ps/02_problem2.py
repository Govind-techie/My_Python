a = int(input("enter your percentage in english : "))
b = int(input("enter your percentage in maths : "))
c = int(input("enter your percentage in science : "))

total_percentage = ((a+b+c)/300)*100

if (a>=33 and b>=33 and c>=33 and (total_percentage)>=40):
    print("Congrats, you are passed in the examination")

else : 
    print("sorry, you failed in your examination")




