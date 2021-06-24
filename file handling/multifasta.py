f=open("/home/akinola/Desktop/Python/file handling/ls_orchid.fasta","r")

#c=open("/home/akinola/Desktop/Python/file handling/result.csv","w")

d=open("/home/akinola/Desktop/Python/file handling/r.tsv","w")

data=f.read()

split_data=data.split(">")
#print(split_data)
for line in split_data:
	if(line!=""):			
		header=line[:line.find("\n")].strip() #  s[:10]
		print(header)
		seq=line[line.find("\n"):].strip()  #s[3:]
		seq=seq.replace("\n","")
		print(seq)
		cA=seq.count("A")
		#print("count of A",cA)
		cT=seq.count("T")
		#print("count of T",cT)
		cG=seq.count("G")
		#print("count of G",cG)
		cC=seq.count("C")
		#print("count of C",cC)
		GC=((cG+cC)/len(seq))*100
		#print("GC content is",GC)
		AT=100-GC
		#print("AT content is",AT)
		#print(header+","+seq+","+str(cA)+","+str(cT)+","+str(cG)+","+str(cC)+","+str(AT)+","+str(GC),file=c)
		#print(header+"\t"+seq+"\t"+str(cA)+"\t"+str(cT)+"\t"+str(cG)+"\t"+str(cC)+"\t"+str(AT)+"\t"+str(GC),file=d)






