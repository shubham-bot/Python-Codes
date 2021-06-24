from Bio import SeqIO

count=SeqIO.convert("/home/akinola/Desktop/Python/biopython/insulin.gb","genbank","/home/akinola/Desktop/Python/biopython/insulin_converted.fasta","fasta")

print("converted records",count)

f=open("/home/akinola/Desktop/Python/biopython/iconverted.fasta","w")
record=SeqIO.read("/home/akinola/Desktop/Python/biopython/insulin_converted.fasta","fasta")

print(">"+str(record.id)+"\n"+str(record.seq),file=f)
