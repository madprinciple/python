fo=open("iplist.txt")
for line in fo:
 print(line.rstrip())
fo.close()


fo=open("iplist.txt")
line1="hi"
while line1:
 line1=fo.readline()
 print(line1.rstrip())
fo.close()
