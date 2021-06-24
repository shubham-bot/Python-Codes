from Bio import SeqIO

handle="/home/akinola/Desktop/Python/biopython/ls_orchid.gbk"

fw=open("/home/akinola/Desktop/Python/biopython/orchid.fasta","w")
record=SeqIO.parse(handle, "genbank")

for data in record:
	print (data.id)
	print(data.seq)
	print(">"+str(data.id)+"\n"+str(data.seq),file=fw)
