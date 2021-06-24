from Bio import SeqIO

handle="/home/akinola/Desktop/Python/biopython/data.fastq"

record=SeqIO.parse(handle,"fastq")
d1={}

list_len=[]
for data in record:
	#print(data.id)
	s=data.seq
	#print("length of seq",len(s))
	d1[data.id]=len(s)#dictionary for id and length of seq
	list_len.append(len(s))
	
#print(list_len)

add=(sum(list_len))


avg=(add/len(list_len))

print("average %0.2f"%avg)chicken gunia
