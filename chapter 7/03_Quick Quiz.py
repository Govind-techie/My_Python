# Quick Quiz: Write a program to print the content of a list using while loops.

list1 = ["govind" , 12 , 34.67 , "mahesh" , None]

a = 0

while(a<len(list1)): # Here, of list1 is 7 so the given condition looks like (a<7)
    print(list1[a]) # Here, [a] act a an index for list1 and we increamenting till the value of a reach its total length of list
    a += 1

