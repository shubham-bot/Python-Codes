s="""CTGGGGACCTGACCCAGCCGCAGCCTTTGTGAACCAACACCTGTGCGGCTCACACCTGGTGGAAGCTCTC
TACCTAGTGTGCGGGGAACGAGGCTTCTTCTACACACCCAAGACCCGCCGGGAGGCAGAGGACCTGCAGG
TGGGGCAGGTGGAGCTGGGCGGGGGCCCTGGTGCAGGCAGCCTGCAGCCCTTGGCCCTGGAGGGGTCCCT
GCAGAAGCGTGGCATTGTGGAACAATGCTGTACCAGCATCTGCTCCCTCTACCAGCTGGAGAACTACTGC
AACTA"""

new_seq=s.replace("\n","")
print(new_seq)

from Bio.Seq import Seq

S1=Seq(new_seq)

print("translate",S1.translate())

print("translate",S1.translate(stop_symbol="-"))	#it will represent stop codon to diff symbol

print("translte",S1.translate(to_stop=True))	#it will print the sequence upto 1st stop codon

print(S1.translate(table=2))

print(S1.translate(table=1))


ob1=Seq("CTGGGGACCTGACCCAGCCGCAGCCTTTGTGAACCAACACCTGTGCGGCTCACACCTGGTGGAAGCTCTCT")


print("original seq",ob1)
print("-1 seq",ob1[:-1])
print("-1 seq",ob1[:-2])
if(len(ob1)%3==0):
	print(ob1.translate())
elif(len(ob1)%3==1):
	print(ob1[:-1].translate())
elif(len(ob1)%3==2):
	print(ob1[:-2].translate())
