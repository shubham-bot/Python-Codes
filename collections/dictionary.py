d={
"gene name":"Gene",
"gene ID":"NC45789",
"gene length":"80000",
"entry date": "20-08-2020",
}

print(d)

#to acess the element from dict using key name


print(d["gene ID"])

#to change the value 

d["entry date"]="1-08-2020"
print(d)

#loop through dictionry

for i in d:
	print(i,d[i])

#keys() ,values()

for a in d.keys():
	print(a)


for b in d.values():
	print(b)

#to check key is present or not

print("coding length" in d)

#add key-value pair in dict
d["coding length"]=5000
print(d)

#to remove the  dict pop()
d.pop("entry date")
print(d)

#to make copy of dict

d2=d.copy()
print(d2)

#nested dictionry

family={
"child1":{
	"name":"a1",
	"age":21
},
"child2":{
	"name":"a2",
	"age":22
},
"child3":{
        "name":"a3",
	"age":23
}
}
print(family)










