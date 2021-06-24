from Bio import SeqIO
from Bio import SeqUtils
handle="/home/akinola/Desktop/Python/biopython/ls_orchid.fasta"
record=SeqIO.parse(handle,"fasta")

for data in record:
	print(data.id)
	print(data.seq)
	print("count of A",data.seq.count("A"))
	print("count of T",data.seq.count("T"))
	print("count of G",data.seq.count("G"))
	print("count of C",data.seq.count("C"))
	print("count of N",data.seq.count("N"))
	print("complement ",data.seq.complement())
	print("reverse complement",data.seq.reverse_complement())
	print("trascription",data.seq.transcribe())
	print("translation",data.seq.translate())
	print("GC content",SeqUtils.GC(data.seq))
	#print("molecular weight",SeqUtils.molecular_weight(data.seq))    optional 
