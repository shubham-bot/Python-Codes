from Bio import SeqIO
fw=open("/home/akinola/Desktop/Python/biopython/feature_orchid.txt","w")
record=SeqIO.parse("/home/akinola/Desktop/Python/biopython/ls_orchid.gbk","genbank")

for data in record:
	print(data.id,file=fw)
	
	for fet in data.features:
		print(str(fet.type)+"---->"+str(fet.location),file=fw)
