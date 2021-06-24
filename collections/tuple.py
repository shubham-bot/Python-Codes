t1=(34,"TACGTA",90,-600,0.45,"hello")

print(t1)

print(type(t1))

#to access the elememts from tuple
print(t1[4])

#negative index
print(t1[-3])


#range of index
print(t1[1:4])

#to change the value in tuple

l1=list(t1)
print(l1)

l1[0]="TGACGCTG"

t=tuple(l1)
print(t)

#loop through tuple
for i in t:
	print(i)

#length of tuple
print(len(t))

#to print even position elements
for i in range(len(t)):
	if(i%2==0):
		print(t[i])

for i in range (len(t)):
	if(i%2!=0):
		print(t[i])

#to check element present or not

print(-600 in t)

#join two tuples
t2=(45,60,80)
t3=t+t2
print(t3)
