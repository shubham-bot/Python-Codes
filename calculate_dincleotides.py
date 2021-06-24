Dna=str(input("enter your sequence ")).upper()

print("select the combinations for calculate AT,AA,AG,GC,GT")

flag="Y"

while(flag=="Y"):
	nucleotide=input("enter your combination")
	if(nucleotide=="AT"):
		c_AT=Dna.count(nucleotide)
		print("count of AT",c_AT)
	elif(nucleotide=="AA"):
		c_AA=Dna.count(nucleotide)
		print("count of AA",c_AA)
	elif(nucleotide=="AG"):
		c_AG=Dna.count(nucleotide)
		print("count of AG",c_AG)
	elif(nucleotide=="GC"):
		c_GC=Dna.count(nucleotide)
		print("count of GC",c_GC)
	elif(nucleotide=="GT"):
		c_GT=Dna.count(nucleotide)
		print("count of GT",c_GT)
	else:
		print("please enter correct combination......")
	flag=input("Do you want to continue...? Y/N").upper()	
	


"""DNA=str(input("enter your sequence")).upper()

print("select the combination for calculate GC,GT,AA")

flag="Y"

while(flag=="Y"):
	nucleotide=input("enter your combination")
	if(nucleotide=="GC"):
		c_GC=Dna.count(nucleotide)
		print("count of GC",c_GC)
	elif(nucleotide=="GT"):
		c_GT=Dna.count(nucleotide)
		print("count of GT",c_GT)
	elif(nucleotide=="AA"):
		c_AA=Dna.count(nucleotide)
		print("count of AA",c_AA)
	else:
		print("please enter correct combination......")
	flag=input("Do you want to continue...? Y/N").upper()"""	
	

