import re
#check your regex here 
pattern="[0-9]+$"
key=input("Enter number: ")
if(re.search(pattern,key)):
    print ("your key in number is", key)
else:
    print ("please key in valid number")