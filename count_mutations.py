seq="ATGCTGATGTGCAATTTAGAGCACTGGTGATTATGCTAGACTGTCATCGGCTGATTTAGCTGCTGATTATGCTGATCATTGCGCATTATGCATGATT"

#ATT,ACTGG,GGGC,GTCATC
"""
if("ACTGGC" in seq):
	cA=seq.count("ACTGGC")
	print("count of ACTGGC",cA)
elif("GGGC" in seq):
	ct=seq.count("GGGC")
	print("count of GGGC",ct)
elif("ATT" in seq):
	cg=seq.count("ATT")
	print("count of ATT",cg)
elif("GTCATCGTACGTAC" in seq):
	cc=seq.count("GTCATCGTACGTAC")
	print("count of GTCATCGTACGTAC",cc)
else:
	print("no any mutations found among them")

"""

if("ATT" in seq):
	c1=seq.count("ATT")
	print("count of ATT",c1)
else:
	print("ATT is not found")
if("ACTGG" in seq):
	c2=seq.count("ACTGG")
	print("count of ACTGG",c2)


mot="ATTGC"


if(mot in dna):
	count_mot=dna.count(mot)
	print("count of mot",count_mot)
else:
	print("not found")
	





