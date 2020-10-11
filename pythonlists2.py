inputs=[]
print("Enter 0 to break the loop")
num=input("enter the values :")
sum=0
while num != '0':
    inputs.append(num)
    num=input("enter the values :")

for i in range(len(inputs)):
    #print (inputs[i])
    sum=sum+int(inputs[i])

print("sum is ", sum)