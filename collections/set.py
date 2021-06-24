s1={45,89,"TACGTCG","AGCT","python"}

print(s1)

#set through loop
for i in s1:
	print(i)
#to check element in set

print("python" in s1)

#add the element in set add()

s1.add(100)
print(s1)

#length of set
print(len(s1))

#remove the element from set remove()
s1.remove("python")
print(s1)


#join two sets union()
s2={67,89,90}

s3=s1.union(s2)

print(s3)

l1=[23,54,23,500,23,54,500,60,23,500,8000,60,800]

s=set(l1)
print(s)
