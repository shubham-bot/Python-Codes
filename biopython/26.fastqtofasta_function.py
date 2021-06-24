from Bio import SeqIO

count=SeqIO.convert("/home/akinola/Desktop/Python/biopython/data.fastq","fastq","/home/akinola/Desktop/Python/biopython/conv.fasta","fasta")

print("converted records",count)
