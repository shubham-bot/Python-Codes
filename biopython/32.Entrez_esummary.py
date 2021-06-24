from Bio import Entrez
from Bio import SeqIO

Entrez.email="aaalafiatayo@mun.ca"

handle=Entrez.esummary(db="Nucleotide",id='XM_009644112.2, XM_035897310.1')

record=Entrez.read(handle)

print(len(record))

print(record)

for data in record:
	print("--------------------------------------------------------")
	for k,v in data.items():
		print(k,v)
