"""
DNA Sequence Analyzer

Takes a DNA sequence as input and reports:
- validity
- base composition and GC/AT content
- purine/pyrimidine counts
- reverse sequence
- complementary strand
- transcribed RNA sequence
- translated protein sequence
"""

print("=" * 55)
print("              DNA SEQUENCE ANALYZER")
print("=" * 55)

dna = input("\nEnter a DNA sequence: ").upper().strip()

if len(dna) == 0:
    print("\n✗ DNA sequence cannot be empty.")
    exit()

valid = True

for base in dna:
    if base not in "ATGC":
        valid = False

if valid:
    print("\n✓ DNA sequence is valid.")
else:
    print("\n✗ DNA sequence is invalid.")
    exit()

print("\n" + "-" * 55)
print("GENERAL INFORMATION")
print("-" * 55)

print(f"Sequence Length : {len(dna)} bp")

print("\n" + "-" * 55)
print("BASE COMPOSITION")
print("-" * 55)

A = dna.count("A")
T = dna.count("T")
G = dna.count("G")
C = dna.count("C")

print(f"A : {A}")
print(f"T : {T}")
print(f"G : {G}")
print(f"C : {C}")

print(f"\nPurines (A+G)     : {A + G}")
print(f"Pyrimidines (T+C) : {T + C}")

GC_percentage = round(((G + C) / len(dna)) * 100, 2)
AT_percentage = round(((A + T) / len(dna)) * 100, 2)

print(f"GC Content : {GC_percentage}%")
print(f"AT Content : {AT_percentage}%")

print("\n" + "-" * 55)
print("SEQUENCE ANALYSIS")
print("-" * 55)

reverse_sequence = dna[::-1]

complementary_strand = ""

for base in dna:
    if base == "A":
        complementary_strand += "T"
    elif base == "T":
        complementary_strand += "A"
    elif base == "G":
        complementary_strand += "C"
    elif base == "C":
        complementary_strand += "G"

RNA_sequence = ""

for base in dna:
    if base == "T":
        RNA_sequence += "U"
    else:
        RNA_sequence += base

print("Reverse Sequence     :", reverse_sequence)
print("Complementary Strand :", complementary_strand)
print("RNA Sequence         :", RNA_sequence)

print("\n" + "-" * 55)
print("PROTEIN TRANSLATION")
print("-" * 55)

codon_table = {
    'UUU':'F','UUC':'F','UUA':'L','UUG':'L',
    'UCU':'S','UCC':'S','UCA':'S','UCG':'S',
    'UAU':'Y','UAC':'Y','UAA':'Stop','UAG':'Stop',
    'UGU':'C','UGC':'C','UGA':'Stop','UGG':'W',

    'CUU':'L','CUC':'L','CUA':'L','CUG':'L',
    'CCU':'P','CCC':'P','CCA':'P','CCG':'P',
    'CAU':'H','CAC':'H','CAA':'Q','CAG':'Q',
    'CGU':'R','CGC':'R','CGA':'R','CGG':'R',

    'AUU':'I','AUC':'I','AUA':'I','AUG':'M',
    'ACU':'T','ACC':'T','ACA':'T','ACG':'T',
    'AAU':'N','AAC':'N','AAA':'K','AAG':'K',
    'AGU':'S','AGC':'S','AGA':'R','AGG':'R',

    'GUU':'V','GUC':'V','GUA':'V','GUG':'V',
    'GCU':'A','GCC':'A','GCA':'A','GCG':'A',
    'GAU':'D','GAC':'D','GAA':'E','GAG':'E',
    'GGU':'G','GGC':'G','GGA':'G','GGG':'G'
}

protein = ""

for i in range(0, len(RNA_sequence) - 2, 3):
    codon = RNA_sequence[i:i+3]

    amino_acid = codon_table.get(codon, "?")

    if amino_acid == "Stop":
        break

    protein += amino_acid

print("Protein Sequence     :", protein)

print("\n" + "=" * 55)
print("Analysis Complete!")
print("=" * 55)
