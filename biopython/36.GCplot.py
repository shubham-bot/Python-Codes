from Bio import SeqIO
from Bio.SeqUtils import GC
from matplotlib import pylab
from pylab import *

gc_values = sorted(GC(rec.seq)for rec in SeqIO.parse("/home/akinola/Desktop/Python/biopython/ls_orchid.fasta", "fasta"))
print(gc_values)
pylab.plot(gc_values)
pylab.title("GC plot")

pylab.xlabel("Genes")
pylab.ylabel("GC%")
pylab.show()
