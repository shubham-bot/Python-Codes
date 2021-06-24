from Bio import SeqIO

handle="/home/akinola/Desktop/Python/biopython/data.fastq"

record=SeqIO.parse(handle,"fastq")
#fw=open("/home/akinola/Desktop/Python/biopython/data_seq.txt","w")
for data in record:
	print(data.id)
	print(data.seq)
	print(data.letter_annotations["phred_quality"]) #The quality are list of integers in a record of letters annotation




