ref_seq="ATCTGATGATCGTGATGTCATTGCTACGTGCTAGCTCGTATTGCAGTGCTAGCGAATTGCTGATCGGTAGCATTGCTGACTGCGCATTGCTGACTTCGTAATTGCTAGCTGCATTGCTAGCTGACTCGATTGC"

mut="ATTGC"

for i in range(len(ref_seq)):
	if(ref_seq.startswith(mut,i)):
		print("position of ATTGC mutations",i)

print("-" * 80)


ref_seq="ATGCTGCTTACTAGTAGCTCTTACGATCCGTTCTTACAAGTCGTCAGTCTTACCTCGAGCTTACCTTACCTTACTCGATACACATCTTACGATCTTAC"

mut="CTTAC"


for i in range(len(ref_seq)):
	if(ref_seq.startswith(mut,i)):
		print("position of CTTAC mutations",i)
