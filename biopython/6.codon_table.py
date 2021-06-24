from Bio.Data import CodonTable

standard_table=CodonTable.unambiguous_dna_by_id[1]
print(standard_table)

mito_table=CodonTable.unambiguous_dna_by_id[2]
print(mito_table)

#by name
s_t=CodonTable.unambiguous_dna_by_name["Standard"]
print(s_t)


print(type(CodonTable.unambiguous_dna_by_name))

print(CodonTable.unambiguous_dna_by_name.keys())


s1=CodonTable.unambiguous_dna_by_name["Thraustochytrium Mitochondrial"]

print(s1)

#print(CodonTable.unambiguous_dna_by_name.values())

print("start codons",s_t.start_codons)

print("stop codons",s_t.stop_codons)
