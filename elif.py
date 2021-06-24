#s1=40 s2=60 s3=600

n1=int(input("enter your 1st number"))

n2=int(input("enter your 2nd number"))

n3=int(input("enter your 3rd number"))

if(n1>n2 and n1>n3):
	print("n1 is a grater number")
elif(n2>n1 and n2>n3):
	print("n2 is a grater number")
elif(n3>n1 and n3>n2):
	print("n3 is grater number")
else:
	print("n1 ==n2==n3")
