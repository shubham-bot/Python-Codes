l1=[345,"TAGCTC",800,"python",-0.89,-600]

print(l1)

#to access the element from the list
print(l1[1])

#range of index
print(l1[2:5])

#to list through loop
for a in l1:
	print(a)

#to change the value from the list
l1[1]="CGCATGCT"
print(l1)


l1[3]="Hello"
print(l1)

#length of list
print(len(l1))

#to check particular element present inside list or not

if(800 in l1):
	print("yes it is present")
else:
	print("it is not present")

#to add the element present inside a list append()
l1.append(700.56)
print(l1)


#to add the element in specifc position insert()
l1.insert(0,"GC")
print(l1)

#to remove the element from list remove()

l1.remove(-600)
print(l1)

#del keyword to remove the element from specif index
del l1[1]
print(l1)

#join two lists
l2=[56,78,90,0.23]

l3=l1+l2

print(l3)

#to reverse the list
l2.reverse()
print(l2)


seq="TATCCGATGCTGACGTAGCTGATCTACGTAGCTGATCGTCGTAGTATCGTAGTCATCGTAGCTAGCTGATGCTAGTCGATGCTAGCTAGCTAGCTGATCTAGCTGAATGCTAGCTATG"

print(list(seq))

print(type(l3))



#sort the list
l2.sort()
print(l2)

