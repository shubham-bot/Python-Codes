f=open("/home/akinola/Desktop/Python/file handling/ls_orchid.fasta","r")

f2=open("/home/akinola/Desktop/Python/file handling/seq.fasta","w")
for line in f:
	if(not line.startswith(">")):
		print(line.strip(),file=f2)
