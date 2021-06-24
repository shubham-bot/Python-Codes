from Bio import SeqIO

handle="/home/akinola/Desktop/Python/biopython/ls_orchid.fasta"

#data=next(SeqIO.parse(handle,"fasta"))
#this next method will give one record at a time if I want 2nd record then we have to use next method again
#print(data.id)


data=SeqIO.parse(handle,"fasta")


for my_data in data:
	print(my_data.id)
	print(my_data.seq)
