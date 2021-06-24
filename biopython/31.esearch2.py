from Bio import Entrez
from Bio import SeqIO

Entrez.email="aaalafiatayo@mun.ca"

handle=Entrez.esearch(db="nucleotide",term="insulin",idtype="acc", retmax="10")

record=Entrez.read(handle)

#print(record)

print(record["IdList"])


