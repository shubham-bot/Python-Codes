f=open("/home/akinola/Desktop/Python/file handling/ls_orchid.fasta","r")

f1=open("/home/akinola/Desktop/Python/file handling/header.txt","w")
for data in f:
	if(data.startswith(">")):
		print(data,file=f1)





