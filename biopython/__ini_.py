class sequence:
	header=""
	seq=""
	
	def __init__(self,header,seq):
		self.header=header
		self.seq=seq

	def rna(self):
		print("rna seq is",self.seq.replace("T","U"))
	def GC(self):
		G=self.seq.count("G")
		C=self.seq.count("C")
		GC=((G+C)/len(self.seq))*100
		print("GC content",GC)
	def AT(self):
		A=self.seq.count("A")
		T=self.seq.count("T")
		AT=((T+A)/len(self.seq))*100
		print("AT content",AT)
	def ATGC(self):
		A=self.seq.count("A")
		T=self.seq.count("T")
		G=self.seq.count("G")
		C=self.seq.count("C")
		print("count of A",A)
		print("count of T",T)
		print("count of G",G)
		print("count of C",C)
	def count_total(self):
		print("total number of nucleotides", len(self.seq))


s1=sequence(">h1","TAGCTGCATCGTAGCTGATCGTAGCTAGTCGATGCTGATCGTAGCTAGTCGATCGTAG")
s1.GC()

s2=sequence(">h2","TAGCGATGAGTCGTGATGCTAGC")
s2.rna()

s3=sequence(">h3","TAGTCATCTGATGGCTGAGTAACGTACGTAGCGACTGATGCTGCTGACTGATGTGC")
s3.ATGC()


s4=sequence(">h4","TACGGGACATAGCTGATCCGGACACAGTTCGACATTGAGAGCAGTGCGACACA")
s4.AT()

s1.count_total()

s5=sequence(">h5","ATGTGACACATGCTGATGCACAGTGACCAGTCGCACATGATAGACAACGGGCCTCGCTA")
s5.rna()
