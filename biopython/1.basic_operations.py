#Bio->package Seq->program
from Bio.Seq import Seq

#Bio->package	.Seq-> program   Seq->class present inside a program

s1=Seq("ATCTGATGTGTTGGCATGTGACGTGCTGATCGTACGTAGCTGATCGTAGCTGATCGTAGCTGTCAGTCGTAGCTGTCAGTCGTGCTAG")
print(s1)

#count A T G C
print("count of A",s1.count("A"))
print("count of T",s1.count("T"))
print("count of G",s1.count("G"))
print("count of C",s1.count("C"))

#lower()
print(s1.lower())

print(s1[3:])

#length of sequence
print(len(s1))


