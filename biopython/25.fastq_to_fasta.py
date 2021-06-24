from Bio import SeqIO

fw=open("/home/akinola/Desktop/Python/biopython/new_data.fasta","w")
record=SeqIO.parse("/home/akinola/Desktop/Python/biopython/data.fastq","fastq")

for data in record:
	print(data.id)
	print(data.seq)
	print(">"+str(data.id)+"\n"+str(data.seq),file=fw)
