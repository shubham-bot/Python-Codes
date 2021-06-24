ref_seq="TACGTGCTAGCATCGTAGCTGACTAGCTGATGATGCTAGCGAGCGACTGATCTAGCTGATCGATCGTAGCTGATCGTAGCTATCGTATGTCGTAGTCGTAGCTGAGCTGACTGATCTAGTGTCTGCTAGTCGTAGCTATCTAGTGCT"

base=["A","T","G","C"]

d1={}

for b1 in base:
	for b2 in base:
		for b3 in base:
			b=b1+b2+b3
			countTri=ref_seq.count(b)
			if(countTri>0):
				d1[b]=countTri
			

print(d1)


"""
1)A A A ->AAA
2)A A   ->AAT
	  AAG
	  AAC
A T A
"""


