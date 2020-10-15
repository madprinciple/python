import re
#test your regex here 
pattern="^[0-9]+\.[0-9]+$"
key=input("Enter number: ")
if(re.search(pattern,key)):
    print ("your number is", key)
else:
    print ("please enter a valid number")