from Bio import SeqIO

handle="/home/akinola/Downloads/sequence(1).fasta"
fw=open("/home/akinola/Desktop/Python/biopython/dna.txt","w")
Data=SeqIO.read(handle, "fasta")

print(Data.id)
print(Data.seq,file=fw)
