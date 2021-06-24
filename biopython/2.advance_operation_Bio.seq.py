from Bio.Seq import Seq

s1=Seq("ATGTCGATGCTAGTGCGATGCTGATCGTACTATCGTACTACTACTGTCGTCGATGCTAGCTGATCGTAGCTATCGATGCTAGCTAGCTGACTGATCGTAGCTAGTCG")

#complement

print("orignal sequence",s1)

print("complement of sequence",s1.complement())

#reverse complement
print("reverse complement of sequence",s1.reverse_complement())

#transcription

print("DNA to RNA",s1.transcribe())

#translation
print("translation",s1.translate())



