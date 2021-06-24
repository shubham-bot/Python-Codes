from Bio import Entrez
from Bio import SeqIO

Entrez.email="aaalafiatayo@mun.ca"

handle= Entrez.esearch(db="pubmed",term="orchid",retmax=463)

record=Entrez.read(handle)

print(record)

print(record["IdList"])





