seq="TAGTGTGCTGTGTGCGCTGACGACATCTAGCTATCGTGATGCTGATGCTGATCGATGCGATCGTAGTCGATCGATCGTAGCTTAGTCGTGCTGATCGATGCTGATGCTGACTGCTAGCTACGTAGCTGCGACTGATCGTACGTAGCTACGTCTGTAGTGCA"
print("orignal sequence",seq)

#ATGC
seq=seq.replace("A","a")	#aTGC
seq=seq.replace("T","A")	#aAGC
seq=seq.replace("a","T")	#TAGC
seq=seq.replace("C","c")	#TAGc
seq=seq.replace("G","C")	#TACc
seq=seq.replace("c","G")	#TACG

print("complement of sequence",seq)

print("reverse complement of sequence",seq[::-1])


