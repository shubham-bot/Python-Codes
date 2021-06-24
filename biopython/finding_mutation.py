"""ref_seq="ATCTGATGATCGTGATGTCATTGCTACGTGCTAGCTCGTATTGCAGTGCTAGCGAATTGCTGATCGGTAGCATTGCTGACTGCGCATTGCTGACTTCGTAATTGCTAGCTGCATTGCTAGCTGACTCGATTGC"

mut="ATTG"

for i in range(len(ref_seq)):
    if ref_seq.startswith(mut, i):
        print(mut,i)"""

ref_seq="AAAAATTGGCCAAAAGGGGGTTTGCACGTAAGCGTTTTTTTGGGGCCAAAAAAAAGCGCGCGCGCGGTAACGTACGTACGTACGT"
mut_seq="AAAAAGTGGCCAAATGGGCGTTCGCTCGTAAGCGTCTTTTTAGGGCCCAAAAGAAGCGCGAGCGCGGTAAAGTACGTACGTATGC"

c_mut=0

for i in range(len(ref_seq)):
    if (ref_seq[i]!= mut_seq[i]):
        print(i)
        print(ref_seq[i], mut_seq[i])
        c_mut +=1
print("count of mutation", c_mut)