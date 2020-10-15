
seperator=[]
number=int(input("Please enter number: "))
quotient=number
while (quotient >= 1000):
    remainder=quotient%1000
    quotient=quotient//1000
    if (remainder == 0):
        seperator.insert(0,"000")
    else:
        seperator.insert(0,str(remainder))

seperator.insert(0,str(quotient))

print(seperator)
print(','.join(seperator))