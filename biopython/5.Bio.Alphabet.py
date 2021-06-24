from Bio.Seq import Seq
from Bio.Alphabet import generic_protein,generic_rna,generic_dna

s1=Seq("ATGCACGAGCGTAGGCCG",generic_protein)
print(s1)
print(s1.alphabet)

s2=Seq("ATGCACGAGCGTAGGCCG",generic_rna)

print(s2.alphabet)

s3=Seq("TAGTCGAGTCGATGCTGCAGC",generic_dna)

print(s3.alphabet)


