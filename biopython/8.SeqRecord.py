from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

sr=SeqRecord("AGCTGACTACGTAGTC",id="NC2001",description="protein",name="ABC")

print(sr.id)
print(sr.seq)
print(sr.description)

print(sr)
