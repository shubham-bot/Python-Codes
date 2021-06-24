f=open("/home/akinola/Desktop/Python/file handling/sequence.fasta","r")

cA=0
cT=0
cG=0
cC=0
for data in f:
	if(data.startswith(">")):
		print(data)
	else:
		#print(data)
		cA=cA+data.count("A")
		cT=cT+data.count("T")
		cG=cG+data.count("G")
		cC=cC+data.count("C")

print("count of A",cA)
print("count of T",cT)
print("count of G",cG)
print("count of C",cC)

GC=((cG+cC)/(cA+cG+cC+cT))*100

print("GC percentage:",GC)

AT=100-GC
print("AT percentage is",AT)

A=((cA)/(cA+cG+cC+cT))*100

print("A percentage", A)

T=((cT)/(cA+cG+cC+cT))*100

print("T percentage", T)

G=((cG)/(cA+cG+cC+cT))*100

print("G percentage", G)

C=((cC)/(cA+cG+cC+cT))*100

print("C percentage", C)
