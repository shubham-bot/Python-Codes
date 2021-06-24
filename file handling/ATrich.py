p=open("/home/akinola/Desktop/Python/file handling/result.csv")

for line in p:
	column=line.replace("\n","").split(",")
	header=column[0]
	seq=column[1]
	AT=column[6]
	GC=column[7]

	if(float(AT)>65):
		print(header+"has High AT content")
	elif(float(AT)<45):
		print(header+"has Low AT content")
	else:
		print(header+"has medium AT content")


	
