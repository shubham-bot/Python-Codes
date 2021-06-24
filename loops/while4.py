#40 to 99
c_E=0
c_O=0


i=40
while(i<=99):
	if(i%2==0):
		print("its a even number",i)
	else:
		print("its a odd number",i)
	i=i+1

print("*" *80)


i=40
while(i<=99):
	if(i%2==0):
		c_E=c_E+1
		
	else:
		c_O=c_O+1
	i=i+1

print("count of even number",c_E)
print("count of odd number",c_O)
