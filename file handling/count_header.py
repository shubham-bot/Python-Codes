f=open("/home/akinola/Desktop/Python/file handling/ls_orchid.fasta","r")

c_H=0

for line in f:
	if(line.startswith(">")):
		#c_H=c_H+1
		c_H +=1

print("count of headers",c_H)
		
