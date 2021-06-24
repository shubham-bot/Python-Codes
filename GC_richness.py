seq=input("enter your sequence")

G=seq.count("G")
C=seq.count("C")

GC=((G+C)/len(seq))*100
print("GC content",GC)

if(GC>=65):
	print("this sequence has high GC content")
elif(GC>50 and GC<65):
	print("this sequence has medium GC content")
else:
	print("this sequence has low GC content")


seq=input("enter your sequence")

A=seq.count("A")
T=seq.count("T")

AT=((A+T)/len(seq))*100
print("AT content",AT)

if(AT>=65):
	print("this sequence has high AT content")
elif(AT>50 and AT<65):
	print("this sequence has medium AT content")
else:
	print("this sequence has low AT content")
