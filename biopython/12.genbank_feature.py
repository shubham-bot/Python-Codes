from Bio import SeqIO

handle="/home/akinola/Desktop/Python/biopython/sequence.gb"

record=SeqIO.read(handle,"genbank") 

print(record.id)

print(record.features)


for feature in record.features:
	print(feature.type,"-->",feature.location)
	print(feature.qualifiers)




print("---------------------------------------------------------------------------------")

print(record.annotations)
print(record.annotations["taxonomy"])
