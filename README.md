# 🧬 DNA Sequence Analyzer

A Python based bioinformatics tool that analyzes DNA sequences by validating nucleotide input, calculating sequence statistics, generating complementary DNA and RNA sequences, and translating coding DNA into its corresponding protein sequence.

This project was developed as part of my journey into **Bioinformatics** and **Computational Biology**, with the goal of strengthening both my Python programming skills and my understanding of the Central Dogma of Molecular Biology.

---

## Features

- ✅ DNA sequence validation
- ✅ Sequence length calculation
- ✅ Nucleotide (A, T, G, C) composition analysis
- ✅ Purine and pyrimidine count
- ✅ GC and AT content calculation
- ✅ Reverse DNA sequence generation
- ✅ Complementary DNA strand generation
- ✅ DNA → mRNA transcription
- ✅ RNA → Protein translation using the standard genetic code

---

## Biological Workflow

```
DNA (Coding Strand)
        │
        ▼
RNA Transcription
        │
        ▼
mRNA Sequence
        │
        ▼
Protein Translation
        │
        ▼
Protein Sequence
```

---

## Project Structure

```
DNA Sequence Analyzer
│
├── Validate DNA sequence
├── Calculate sequence statistics
├── Generate reverse sequence
├── Generate complementary strand
├── Transcribe DNA into RNA
└── Translate RNA into protein
```

---

## Technologies Used

- Python 3
- String Manipulation
- Loops
- Conditional Statements
- Dictionaries
- Basic Bioinformatics Algorithms

---

## Example

### Input

```
ATGGCCATTGTAATGGGCCGCTGA
```

### Output

```
DNA sequence is valid.

Sequence Length : 24 bp

Base Composition
----------------
A : 5
T : 6
G : 8
C : 5

Purines (A+G)     : 13
Pyrimidines (T+C) : 11

GC Content : 54.17%
AT Content : 45.83%

Reverse Sequence
AGTCGCCGGGTAATGTTACCGGTA

Complementary Strand
TACCGGTAACATTACCCGGCGACT

RNA Sequence
AUGGCCAUUGUAAUGGGCCGCUGA

Protein Sequence
MAIVMGR
```

---

## How It Works

### 1. DNA Validation

The program first verifies that the input sequence contains only valid DNA nucleotides:

- Adenine (A)
- Thymine (T)
- Guanine (G)
- Cytosine (C)

If invalid characters are detected, the program terminates.

---

### 2. Sequence Analysis

The analyzer computes:

- Sequence length
- Number of each nucleotide
- Purine count
- Pyrimidine count
- GC percentage
- AT percentage

---

### 3. Reverse Sequence

The DNA sequence is reversed to provide the nucleotide order from end to beginning.

---

### 4. Complementary Strand

Each nucleotide is replaced with its complementary base.

| DNA | Complement |
|-----|------------|
| A | T |
| T | A |
| G | C |
| C | G |

---

### 5. RNA Transcription

Assuming the input DNA is the **coding (sense) strand**, transcription is performed by replacing:

```
T → U
```

---

### 6. Protein Translation

The RNA sequence is translated into amino acids using the **Standard Genetic Code**.

Translation:

- reads three nucleotides (one codon) at a time,
- begins from the first codon,
- terminates when a stop codon is encountered.

---

## Learning Outcomes

This project helped strengthen my understanding of:

- Python programming
- Dictionaries and string manipulation
- Biological sequence analysis
- DNA transcription
- Protein translation
- Fundamental bioinformatics concepts

---

## Author

**Harshit Mishra**

Aspiring Bioinformatics student with an interest in computational biology, genomics, machine learning, and biomedical data analysis.

---

## License

This project is licensed under the MIT License.
