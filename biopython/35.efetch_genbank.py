from Bio import Entrez
from Bio import SeqIO


Entrez.email=""

handle=Entrez.efetch(db="nucleotide",id="EU490707",rettype="gb",retmode="text")

print(handle.read())
