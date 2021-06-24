from Bio import Entrez
from Bio import SeqIO

Entrez.email="aaalafiatayo@mun.ca"

handle1=Entrez.esearch(db="nucleotide",term="insulin",idtype="acc", retmax="10")

record1=Entrez.read(handle1)

#print(record)

print(record1["IdList"])

handle=Entrez.esummary(db="Nucleotide",id=', '.join(record1["IdList"]))

record=Entrez.read(handle)

print(len(record))

print(record)

for data in record:
	print("--------------------------------------------------------")
	for k,v in data.items():
		print(k,v)

