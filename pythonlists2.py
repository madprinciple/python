import re
inputs=[]
print("Enter 0 to break the loop")
num=input("enter the values :")
sum=0
while num != '0':
    if(re.search("^[0-9]+$",num)):
        inputs.append(num)
    else:
        print("Please entert only the numbers !!")
    
    num=input("enter the values :")

for i in range(len(inputs)):
    #print (inputs[i])
    sum=sum+int(inputs[i])

print("sum is ", sum)