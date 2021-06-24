from Bio import SeqIO

record=SeqIO.read("/home/akinola/Desktop/Python/biopython/sequence.fasta","fasta")

print(record.id)
print(record.name)
print(record.description)
print(record.seq)
print(record)   
