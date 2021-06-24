seq="TAGTGTGCTGTGTGCGCTGACGACATCTAGCTATCGTGATGCTGATGCTGATCGATGCGATCGTAGTCGATCGATCGTAGCTTAGTCGTGCTGATCGATGCTGATGCTGACTGCTAGCTACGTAGCTGCGACTGATCGTACGTAGCTACGTCTGTAGTGCA"


#ATGC
seq=seq.replace("A","a")	#aTGC
seq=seq.replace("T","A")	#aAGC
seq=seq.replace("a","T")	#TAGC
seq=seq.replace("C","c")	#TAGc
seq=seq.replace("G","C")	#TACc
seq=seq.replace("c","G")	#TACG

print(seq)


Seq_comp="ATGCGATACGATGACTACGATGCTGAGTTAAGCCGTAGTTGACAGTCGTAGCTGATCTTGACTGATCGTAGCTCCAATTGATGTACCACACA"

#ATGC

Seq_comp=Seq_comp.replace("A","a")	#aTGC
Seq_comp=Seq_comp.replace("T","A")	#aAGC
Seq_comp=Seq_comp.replace("a","T")	#TAGC
Seq_comp=Seq_comp.replace("C","c")	#TAGc
Seq_comp=Seq_comp.replace("G","C")	#TACc
Seq_comp=Seq_comp.replace("c","G")	#TACG

print(Seq_comp)

