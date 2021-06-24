from Bio import Entrez
from Bio import SeqIO

Entrez.email ="aaalafiatayo@mun.ca"

handle=Entrez.einfo(db="pubmed")

result=Entrez.read(handle)

#print(result)
print(result["DbInfo"]["Description"])

print(result["DbInfo"]["Count"])

print(result["DbInfo"]["LastUpdate"])

