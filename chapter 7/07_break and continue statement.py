# THE BREAK STATEMENT

# ‘break’ is used to come out of the loop when encountered. It instructs the program to –
# exit the loop now.


for i in range(100):
    if(i == 50):
        break # break statement exit the loop right when the condition for if statement gets True
    print(i)



# THE CONTINUE STATEMENT
# ‘continue’ is used to stop the current iteration of the loop and continue with the next
# one. It instructs the Program to “skip this iteration”.



for i in range(100):
    if(i == 50):
        continue # continue statement skips th given iteration or value  from the loop right when the condition for if statement gets True
    print(i)

    # Note : in output it does not give value 50 because of continue statement




