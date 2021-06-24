from Bio import motifs
from Bio.Seq import Seq

DNA_motif=[Seq("AGCT"),Seq("TCGA"),Seq("AACT")]

seq=motifs.create(DNA_motif)

print(seq)

print(seq.counts)

print(seq.counts["A",:])

print(seq.consensus)

print(seq.anticonsensus)

seq.weblogo("/home/akinola/Desktop/Python/biopython/seq.png")
