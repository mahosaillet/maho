
# Function for transcribing DNA into mRNA
def transcription(DNA_strand):
    mRNA = []  # Create an empty list for mRNA
    for nucleotide in DNA_strand:
        if nucleotide == 'A':
            mRNA.append('U')  # Replace 'A' with 'U' in mRNA
        elif nucleotide == 'T':
            mRNA.append('A')  # Replace 'T' with 'A' in mRNA
        elif nucleotide == 'G':
            mRNA.append('C')  # Replace 'G' with 'C' in mRNA
        else:
            mRNA.append('G')  # Replace 'C' with 'G' in mRNA
    return ''.join(mRNA)  # Convert the mRNA list into a string

# Function to find the initiation codon and return the mRNA sequence from that codon
def find_start_codon(sequence):
    length = len(sequence)
    index = 0
    while index < length and sequence[index:index + 3] != "AUG":
        index += 1
    return sequence[index:]  # Return the mRNA sequence starting from the initiation codon (AUG)

# Codon-to-amino acid correspondence table (list of lists)
genetic_code = [
    ["UUU", "Phe"], ["UUC", "Phe"],
    ["CUU", "Leu"], ["CUC", "Leu"], ["CUA", "Leu"], ["CUG", "Leu"], ["UUA", "Leu"], ["UUG", "Leu"],
    ["AUU", "Ile"], ["AUC", "Ile"], ["AUA", "Ile"],
    ["AUG", "Met"],
    ["GUU", "Val"], ["GUC", "Val"], ["GUA", "Val"], ["GUG", "Val"],
    ["UCU", "Ser"], ["UCC", "Ser"], ["UCA", "Ser"], ["UCG", "Ser"], ["AGU", "Ser"], ["AGC", "Ser"],
    ["CCU", "Pro"], ["CCC", "Pro"], ["CCA", "Pro"], ["CCG", "Pro"],
    ["ACU", "Thr"], ["ACC", "Thr"], ["ACA", "Thr"], ["ACG", "Thr"],
    ["GCU", "Ala"], ["GCC", "Ala"], ["GCA", "Ala"], ["GCG", "Ala"],
    ["UAA", "STOP"], ["UAG", "STOP"], ["UGA", "STOP"],
    ["UAU", "Tyr"], ["UAC", "Tyr"],
    ["CAU", "His"], ["CAC", "His"],
    ["CAA", "Gln"], ["CAG", "Gln"],
    ["AAU", "Asn"], ["AAC", "Asn"],
    ["AAA", "Lys"], ["AAG", "Lys"],
    ["GAU", "Asp"], ["GAC", "Asp"],
    ["GAA", "Glu"], ["GAG", "Glu"],
    ["UGU", "Cys"], ["UGC", "Cys"],
    ["UGG", "Trp"],
    ["CGU", "Arg"], ["CGC", "Arg"], ["CGA", "Arg"], ["CGG", "Arg"], ["AGA", "Arg"], ["AGG", "Arg"],
    ["GGU", "Gly"], ["GGC", "Gly"], ["GGA", "Gly"], ["GGG", "Gly"]
]

# Function to translate mRNA into protein
def translate_mRNA_to_protein(mRNA):
    protein = ""
    for i in range(0, len(mRNA), 3):
        codon = mRNA[i:i + 3]
        for genetic_codon, amino_acid in genetic_code:
            if codon == genetic_codon:
                if amino_acid == "STOP":
                    return protein  # Stop translation if a STOP codon is encountered
                protein += amino_acid
                break
    return protein

# DNA strand sequence to be transcribed and translated
DNA_strand_TAS2R38 = 'CTCTTCACTGTAGTACAACTGAGATTGAGCGTAGGCGTGACACAGGATACTTCAGTCCTCATGTAAAGACAAGTAAAGTCAGGACCTCAAACGTCACCCCAAAGACTGGTTACGGAAGCAAAAGAACCACTTAAAAACCCTACATCACTTCTCCGTCGGTGACTCGTTGTCACTAACACACGACGACACAGAGTCGTAGTCGGCCGAAAAGGACGTACCTGACGACAAGGACTCACGATAGGTCGAATGGGTGAAGGTCTTCAACTCACTTGGTGACTTGGTGTCGATGGTTCGGTAGTAGTACGATACCTACTAACGTTTGGTTCGGTTGGAGACCGAACGACGGACGGAGTCGGACGAAATGACGAGGTTCGAGTAGGCAAAGAGAGTGTGGAAGGACTAGACGAACCGTTCGACCCAGAGGTCCTTCTAGAGGGTCTACGAGGACCCATAATAAGAAACGAGGACGTAGACGTGACAGGAGACACAAACCACGAAAAAATCGTCTGGAGTGAAGTGTCAGTGTTGACACGATAAGTACTTATTGTTATGTTCCGAGTTGACCGTCTAATTTCTAGAGTTAAATAAAATAAGGAAAGAGAAGACGATAGACACCAGACACGGAGGAAAGGATAACAAAGACCAAAGAAGACCCTACGACTGACAGAGGGACCCTTCCGTGTACTCCTGTTACTTCCAGATATGGTCTTTGAGAGCACTGGGGTCGGACCTCCGGGTGTAATTTCGGGAGTTCAGAGAACAGAGGAAAAAGACGAAGAAACACTATAGTAGGACACGACGGAAGTAGAGACACGGGGATGACTAAGACACCGCGCTGTTTTATCCCCACTACCAAACACAACCCTATTACCGTCGAACAGGGAGACCCGTACGTCGGCAGGACTAGAGTCCGTTACGGTTCAACTCCTCTCGACACTACTGGTAAGACGAGACCCGAGTCTCGTCGGACTTCCATTCTCGGCTGGTGTTCCGTCTAAGGGCCTGTGACACGACTTATTAT'

# Transcribe DNA into mRNA
mRNA_TAS2R38 = transcription(DNA_strand_TAS2R38)

# Find the initiation codon and get the mRNA sequence from that point
mRNA_START = find_start_codon(mRNA_TAS2R38)

# Translate mRNA into protein
protein_TAS2R38 = translate_mRNA_to_protein(mRNA_START)

# Display the results
print("mRNA TAS2R38: " + mRNA_TAS2R38)
print("Protein TAS2R38: " + protein_TAS2R38)