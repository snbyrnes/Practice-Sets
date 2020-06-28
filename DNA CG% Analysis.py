# get DNA sequence
dna = input("Enter your DNA Sequence: ")
no_c = dna.count("c")
no_g = dna.count("g")
dna_length = len(dna)
gc_percent = (no_c + no_g) * 100 / dna_length
print("This DNA GC content is",round(gc_percent, 2,),"%")

