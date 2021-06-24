DNA_seq = str(input("Enter your sequence  ")).upper()
print("Select the combination to calculate AA, AT, GC")

flag = "Y"

while (flag=="Y"):
    nucleotides= input("Enter your nucleotide combination  ")
    if(nucleotides=="AA"):
        c_AA=DNA_seq.count(nucleotides)
        print("count of nucleotide", c_AA)
    elif(nucleotides=="AT"):
        c_AT=DNA_seq.count(nucleotides)
        print("count of AT", c_AT)
    elif(nucleotides=="GC"):
        c_GC=DNA_seq.count(nucleotides)
        print("count of GC", c_GC)
    else:
        print("Enter the correct combination......")
    flag=(input("Do you want to continue....Y/N  ")).upper()

