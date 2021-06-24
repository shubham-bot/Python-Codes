from Bio import SeqIO

handle=str(input("enter the path of the fasta file for the processing"))

record=SeqIO.read(handle,"fasta")

print(record.id)

print(record.seq)

print("count of A",record.seq.count("A"))

print("count of G",record.seq.count("G"))

print("count of T",record.seq.count("T"))

print("count of C",record.seq.count("C"))

print("complement of seq",record.seq.complement())


print("reverse complement of seq", record.seq.reverse_complement())

print("trasncription",record.seq.transcribe())

#print("translation",record.seq.translate())

if(len(record.seq)%3==0):
	print(record.seq.translate())
elif(len(record.seq)%3==1):
	print(record.seq[:-1].translate())
elif(len(record.seq)%3==2):
	print(record.seq[:-2].translate())
