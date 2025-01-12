a = input("enter your comment : ")

message1 = "Make a lot of money"
message2 = "buy now"
message3 = "subscribe this"
message4 = "click this"

if((message1 in a) or (message2 in a) or (message3 in a) or (message4 in a)):
    print("its a spam comment!!",(a))
    
else:
    print("its not spam comment",(a))
 
#  Note : in command or statement checks whether a given string is presnt in another given string