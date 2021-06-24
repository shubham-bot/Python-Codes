from Bio import SeqIO

handle="/home/akinola/Desktop/Python/biopython/ls_orchid.gbk"

data=SeqIO.parse(handle, "genbank")

for record in data:

	print(record.id)
	print(record.seq)
	print(record.description)
	print(record.name)
	print(record.annotations)
