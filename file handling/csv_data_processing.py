f=open("/home/akinola/Desktop/Python/file handling/result.csv","r")

for line in f:
	column=line.replace("\n","").split(",")
	#print(column)
	header=column[0]
	seq=column[1]
	AT=column[6]
	GC=column[7]

	if(float(GC)>65):
		print(header+"has High GC content")
	elif(float(GC)<45):
		print(header+"has Low GC content")
	else:
		print(header+"has medium GC content")
