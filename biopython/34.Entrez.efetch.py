from Bio import Entrez
from Bio import SeqIO


Entrez.email="aaalafiatayo@mun.ca"

handle=Entrez.efetch(db="nucleotide",id="EU490707",rettype="fasta")

record=SeqIO.read(handle,"fasta")

print(record)

print(record.id)

print(record.seq)
