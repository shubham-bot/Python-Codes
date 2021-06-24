
"""def fetch_header(path):
	l=[]
	f=open(path,"r")
	for line in f:
		if(line.startswith(">")):
			l.append(line.strip())
	return l
			
path=str(input("enter your path of file for processiong"))
l=fetch_header(path)
#print(l)
for list_el in l:
	print(list_el)
"""

def count_ATGC(path):
	l1=[]
	f=open(path,"r")
	data=f.read()

	split_data=data.split(">")
	#print(split_data)
	for line in split_data:
		if(line!=""):			
			header=line[:line.find("\n")].strip() #  s[:10]
			print(header)
			seq=line[line.find("\n"):].strip()  #s[3:]
			seq=seq.replace("\n","")
			#print(seq)
			ot_line=header+"\t"+str(seq.count("A"))+"\t"+str(seq.count("T"))+"\t"+str(seq.count("C"))+"\t"+str(seq.count("G"))
			l1.append(ot_line)
	return l1


path=input("enter the path for processing")
l1=count_ATGC(path)
for c in l1:
	print(c) 
