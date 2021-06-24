ref_seq="AGCTGACTATCGTACTGATCTAGCTATGCTGACTGCTGATCGATGCTGTGATGCTATCGATGCTAGTCGATCGTACTGATCGTAGCTGATCGTAGCTATCGATGCTAGCTAGCTGCTAGTCGATCGAGTCTAGCTAGTCATGTCGACACTAGCTAGCTAGC"

base=["A","T","G","C"]

l1=[]
l2=[]
for b1 in base:
	for b2 in base:
		b=b1+b2
		l1.append(b)
		count=ref_seq.count(b)
		l2.append(count)
		#print("count of "+b+"="+str(count))
print("dinucaleotides",l1)
print("count ",l2)


"""
b1  b2
A   A	AA
A   T   AT
A   G   AG
A   C   AC
T   A   TA
T   T   TT
T   C   TC
T   G   TG
C
:
:
:
"""
seq="ATCGTCGACTGA"

l_d=[]
lc=[]

base=["A","T","G","C"]

for b1 in base:
	for b2 in base:
		b=b1+b2
		c1=seq.count(b)
		l_d.append(b)
		lc.append(c1)
print(l_d)
print(lc)
		


