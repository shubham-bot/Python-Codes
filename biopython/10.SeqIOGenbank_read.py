from Bio import SeqIO


handle="/home/akinola/Desktop/Python/biopython/sequence.gb"
record=SeqIO.read(handle,"genbank")
print(record.id)
print(record.seq)
print(record.description)
print(record.name)
print(record.annotations)
