from Bio.Seq import Seq

s1=Seq("ATGTCGATGCTAGTGCGATGCTGATCGTACTATCGTACTACTACTGTCGTCGATGCTAGCTGATCGTAGCTATCGATGCTAGCTAGCTGACTGATCGTAGCTAGTCG")

#complemnt

#print(s1.complement())

#print(s1.reverse_complement())

#print(s1.transcribe())

#print(len(s1))

#print(s1.translate())


dna_seq="""CTGGGGACCTGACCCAGCCGCAGCCTTTGTGAACCAACACCTGTGCGGCTCACACCTGGTGGAAGCTCTC
TACCTAGTGTGCGGGGAACGAGGCTTCTTCTACACACCCAAGACCCGCCGGGAGGCAGAGGACCTGCAGG
TGGGGCAGGTGGAGCTGGGCGGGGGCCCTGGTGCAGGCAGCCTGCAGCCCTTGGCCCTGGAGGGGTCCCT
GCAGAAGCGTGGCATTGTGGAACAATGCTGTACCAGCATCTGCTCCCTCTACCAGCTGGAGAACTACTGC
AACTA"""

dna_seq1=dna_seq.replace("\n","")

print(dna_seq1)

from Bio.Seq import Seq

w=Seq(dna_seq1)

print(w.translate())

print(w.translate(stop_symbol="-")) 
