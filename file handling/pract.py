seq=open("/home/akinola/Downloads/sequence.fasta", "r")

#print(seq.read())

"""print(seq.readline())
print(seq.readline())
print(seq.readline())
print(seq.readline())"""

#for i in seq:
#	print(i)

#print(seq.read(100))


"""orchd_seq=open("/home/akinola/Downloads/ls_orchid.fasta", "r")

for data in orchd_seq:
	if(data.startswith(">")):
		print(data)



orchd_seq=open("/home/akinola/Downloads/ls_orchid.fasta","r")

orchd_headers=open("/home/akinola/Downloads/heads.txt","w")

for data in orchd_seq:
	if (data.startswith(">")):
		print(data,file=orchd_headers)"""


#seq=open("/home/akinola/Downloads/sequence.fasta", "r")

nucleo_base=open("/home/akinola/Downloads/base_fasta.txt", "w")

seq=open("/home/akinola/Desktop/Python/file handling/ls_orchid.fasta", "r")

#for line in seq:
	#if(not line.startswith(">")):
		#print(line)


"""for line in seq:
	if(not line.startswith(">")):
		print(line.strip())"""


"""for line in seq:
	if(not line.startswith(">")):
		print(line.strip(), file=nucleo_base)"""


#count headers

"""no_heads=0

for line in seq:
	if(line.startswith(">")):
		no_heads=no_heads+1

print("count of headers", no_heads)"""


"""name=input("Please, enter your name: ")

if (name=="Akin"):
	print("Thanks {0}, you are good to go!".format(name))
else:
	print("This is a name mismatch")"""


dna_seq="""ATGCTGATCGTAGCTGATGCGTAGTCGATGTGTACTAGCTGATGATTGCATTGCCAGCTGATCGTACTGACGTACGTGTCGTATGCTAGTCGTAGCTGATCGTGCTGATCGTAGCTGATGCTAGTCGATCGT
TGATGCTGATCGTAGCTGACTGATCGTAGCGAATTGCTCGTAGCTGATGCTAGCTATCTAGCTATGCTGCTATCTAGCTATGCTAGCTAGCTGATCATCGTACTTGCTCGTAGCTAGCAGCTGCATTGCTAGCTCGTAGC
TGATCGTAGCTGTAGTGCTAGTCGAATTGCTACTGATGCTGATCGTAGCTATCGTAGCTGATGCTGATGTACATTGCTGATCGTAGGTAGCTGATGCGATCGCGATATTGCTGATCGTGTAGTCGATGCTAGTCGATGCTAGC
TGATCTGCTGATGTCTAGCTGATCGTAGCTAGTCGATCTGCGATATTGCGTGTGGTGTGTTGTGTTATTGCAGCTGATGCTGATCGTAGCTGATCATTGCTAGCTGCTGTAGTGATCGTAGCTGATTGCATGCTATTGC
TGATCGTACTGCTGACTGCATTGC"""

mutation="ATTGC"

if mutation in dna_seq:
	d=("{} is in {}".format(mutation,"dna_seq"))
	print(d) 
	#count number of mutation

if mutation in dna_seq:
	c_mutation=dna_seq.count(mutation)
	print("The number of mutation =", c_mutation)

else:
	print("This mutation is absent")
	

"""name = input("Please enter your name: ")
age = int(input("How old are you? ".format(name))

if age<18 and age< 31:
	print("Wellcome to our holiday program".format(name))
else:
	print("You age is out of range")"""

	






















