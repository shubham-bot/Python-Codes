ref_seq="AAAAATTGGCCAAAAGGGGGTTTGCACGTAAGCGTTTTTTTGGGGCCAAAAAAAAGCGCGCGCGCGGTAACGTACGTACGTACGT"#50
mut_seq="AAAAAGTGGCCAAATGGGCGTTCGCTCGTAAGCGTCTTTTTAGGGCCCAAAAGAAGCGCGAGCGCGGTAAAGTACGTACGTATGC"

c_mut=0
for i in range(len(ref_seq)):
	if(ref_seq[i]!=mut_seq[i]):
		print(i)
		print(ref_seq[i],mut_seq[i])
		c_mut=c_mut+1
print("count of point mutations",c_mut)



"""
i=0	if(if(ref_seq[0]!=mut_seq[0]):	A==A (F)
i=1	if(ref_seq[1]!=mut_seq[1]):	A==A(F)
i=2	if(ref_seq[2]!=mut_seq[2]):	A==A(F)
i=3	if(ref_seq[3]!=mut_seq[3]):	A==A(F)
i=4	if(ref_seq[4]!=mut_seq[4]):	A==A(F)
i=5     if(ref_seq[5]!=mut_seq[5]):	T==G(T)	c_mut=0+1=1"""



ref_seq="TCGACATGCAATGAGTCATAGCTACGT"
mut_seq="TAGACATTCAAAGAGACATACCTATGA"

for i in range(len(ref_seq)):
	if(ref_seq[i]!=mut_seq[i]):
		print(i)
		print(ref_seq[i],mut_seq[i])
		c_mut=c_mut+1
print("count of point mutations",c_mut)
