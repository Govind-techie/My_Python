#  Write a python function to remove a given word from a list ad strip it at the same time.



def remove(list1 , word):
    n = []
    for item in list1:
        if not (item == word):
            n.append(item.strip(word))
    return n
        
        
      

list1 = ["Govind","Mahesh","Rakesh","ind"]

print(remove(list1 , "ind"))

