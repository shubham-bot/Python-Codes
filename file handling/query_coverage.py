"""
eml=(length-mismatch-gap)
qc=(eml/ql)*100
"""

f=open("/home/akinola/Desktop/Python/file handling/blast_result.txt","r")

for col in f:
	col=col.strip().split("\t")
	#print(col)
	length=int(col[3])
	mismatch=int(col[4])
	gap=int(col[5])
	EML=length-mismatch-gap
	print("extract matching length:",EML)
	QL=int(col[-1])
	qc=(EML/QL)*100
	print("Query coverage", qc)
