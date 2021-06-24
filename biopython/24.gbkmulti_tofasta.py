from Bio import SeqIO
count=SeqIO.convert("/home/akinola/Desktop/Python/biopython/ls_orchid.gbk","genbank","/home/akinola/Desktop/Python/biopython/new.fasta", "fasta")

print(count)

