#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 13:31:18 2023

@author: mahosaillet
"""

"""
Project: DNA Sequence Processor
Description: This program transcribes DNA sequences into mRNA, translates mRNA into protein sequences,
and allows users to save DNA sequences to a file.
Author: [Maho Saillet]
"""

# Function for transcribing DNA into mRNA
def transcription(DNA_strand):
    """
    Input: DNA_strand (string) - The input DNA sequence to be transcribed.
    Process: Transcribes the DNA sequence into mRNA by replacing nucleotides: A -> U, T -> A, G -> C, C -> G.
    Output: mRNA sequence (string) - The transcribed mRNA sequence.
    """
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
    """
    Input: sequence (string) - The input mRNA sequence.
    Process: Finds the initiation codon "AUG" in the mRNA sequence.
    Output: mRNA sequence from the initiation codon (string).
    """
    length = len(sequence)
    index = 0
    while index < length and sequence[index:index + 3] != "AUG":
        index += 1
    if index < length:
        return sequence[index:]  # Return the mRNA sequence starting from the initiation codon (AUG)
    else:
        return ""  # Return an empty string if the initiation codon is not found
    
    

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
    """
    Input: mRNA (string) - The input mRNA sequence to be translated into protein.
    Process: Translates mRNA into protein sequences using the genetic code.
    Output: Protein sequence (string) - The translated protein sequence.
    """
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


# Function to save DNA sequence to a file
def save_to_file(DNA_strand):
    """
    Input: DNA_strand (string) - The input DNA sequence to be saved to a file.
    Process: Writes the DNA sequence to the file sequence.txt.
    Output: None
    """
    with open("sequence.txt", "w") as file:
        file.write(DNA_strand)


# Function for the menu
def menu():
    print("Menu:")
    print("1. Transcribe DNA sequence to mRNA")
    print("2. Translate mRNA sequence to Protein")
    print("3. Create a DNA Sequence File")
    print("4. Exit")



# Main function
def main():
    """
    Input: None (user input will be received interactively)
    Process: Provides a menu for the user to choose actions, including transcription, translation, and saving to a file.
    Output: None (results will be printed or saved to a file)
    """
    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            DNA_strand = input("Enter DNA sequence: ")
            mRNA = transcription(DNA_strand)
            print("mRNA: " + mRNA)
        elif choice == "2":
            mRNA = input("Enter mRNA sequence: ")
            protein = translate_mRNA_to_protein(mRNA)
            print("Protein: " + protein)
        elif choice == "3":
            DNA_strand = input("Enter the DNA sequence to save in the file: ")
            save_to_file(DNA_strand)
            print("DNA sequence has been saved in the file sequence.txt.")
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

# Run the main function
main()

# DNA strand sequence to be transcribed and translated
DNA_strand_TAS2R38 = 'CTCTTCACTGTAGTACAACTGAGATTGAGCGTAGGCGTGACACAGGATACTTCAGTCCTCATGTAAAGACAAGTAAAGTCAGGACCTCAAACGTCACCCCAAAGACTGGTTACGGAAGCAAAAGAACCACTTAAAAACCCTACATCACTTCTCCGTCGGTGACTCGTTGTCACTAACACACGACGACACAGAGTCGTAGTCGGCCGAAAAGGACGTACCTGACGACAAGGACTCACGATAGGTCGAATGGGTGAAGGTCTTCAACTCACTTGGTGACTTGGTGTCGATGGTTCGGTAGTAGTACGATACCTACTAACGTTTGGTTCGGTTGGAGACCGAACGACGGACGGAGTCGGACGAAATGACGAGGTTCGAGTAGGCAAAGAGAGTGTGGAAGGACTAGACGAACCGTTCGACCCAGAGGTCCTTCTAGAGGGTCTACGAGGACCCATAATAAGAAACGAGGACGTAGACGTGACAGGAGACACAAACCACGAAAAAATCGTCTGGAGTGAAGTGTCAGTGTTGACACGATAAGTACTTATTGTTATGTTCCGAGTTGACCGTCTAATTTCTAGAGTTAAATAAAATAAGGAAAGAGAAGACGATAGACACCAGACACGGAGGAAAGGATAACAAAGACCAAAGAAGACCCTACGACTGACAGAGGGACCCTTCCGTGTACTCCTGTTACTTCCAGATATGGTCTTTGAGAGCACTGGGGTCGGACCTCCGGGTGTAATTTCGGGAGTTCAGAGAACAGAGGAAAAAGACGAAGAAACACTATAGTAGGACACGACGGAAGTAGAGACACGGGGATGACTAAGACACCGCGCTGTTTTATCCCCACTACCAAACACAACCCTATTACCGTCGAACAGGGAGACCCGTACGTCGGCAGGACTAGAGTCCGTTACGGTTCAACTCCTCTCGACACTACTGGTAAGACGAGACCCGAGTCTCGTCGGACTTCCATTCTCGGCTGGTGTTCCGTCTAAGGGCCTGTGACACGACTTATTAT'


