from Bio import SeqIO

handle="/home/akinola/Desktop/Python/biopython/insulin.gb"

f=open("/home/akinola/Desktop/Python/biopython/insulin.fasta","w")
record=SeqIO.read(handle,"genbank")

print(record.id)
print(record.seq)

print(">"+str(record.id)+"\n"+str(record.seq),file=f)
