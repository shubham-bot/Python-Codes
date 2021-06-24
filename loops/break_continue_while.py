#break statment:-we can break the loop even while condition is true

i=1
while(i<=15):
	print(i)
	if(i==7):
		break
	i=i+1


i=10
while(i<=100):
	print(i)
	if(i==80):
		break

	i=i+10

print("------------------------------------------------------------------------")

#continue statement:- we can stop the current iteration and continue with next iteration.

i=0
while(i<=20):
	i=i+1
	if(i==10):
		continue
	print(i)



i=5
while(i<=50):
	i=i+2
	if(i==35):
		continue
	print(i)
print("--------------------------------------------------------------------")
#you can use the else statement with the while loop

i=1
while(i<=5):
	print("python",i)
	i=i+1
else:
	print("its a finished")
