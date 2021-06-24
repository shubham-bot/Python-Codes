from Bio import Entrez
from Bio import SeqIO
#einfo() it gives the all avaliable database list

Entrez.email="aaalafiatayo@mun.ca"	#always tell to ncbi who we are

handle=Entrez.einfo()#it prints all avaliable database lists but its in xml format

#result=handle.read()	#to read xml data we used read methods from SeqIO

#print(result)

data=Entrez.read(handle)#it will convert data into xml to python objects 

print(data)

print(data.keys())

print(data.values())
