#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 17:44:19 2023

@author: mahosaillet
"""

# Dictionary for DNA to RNA base conversion
dna_to_rna = {
    'A': 'U',
    'T': 'A',
    'C': 'G',
    'G': 'C'
}

# Dictionary for RNA codon to amino acid conversion
rna_to_amino_acid = {
    'UUU': 'Phenylalanine',
    'UUC': 'Phenylalanine',
    'UUA': 'Leucine',
    'UUG': 'Leucine',
    'CUU': 'Leucine',
    'CUC': 'Leucine',
    'CUA': 'Leucine',
    'CUG': 'Leucine',
    'AUU': 'Isoleucine',
    'AUC': 'Isoleucine',
    'AUA': 'Isoleucine',
    'AUG': 'Methionine',
    'GUU': 'Valine',
    'GUC': 'Valine',
    'GUA': 'Valine',
    'GUG': 'Valine',
    'UCU': 'Serine',
    'UCC': 'Serine',
    'UCA': 'Serine',
    'UCG': 'Serine',
    'CCU': 'Proline',
    'CCC': 'Proline',
    'CCA': 'Proline',
    'CCG': 'Proline',
    # ... Add the rest of the codon to amino acid mappings
}

def transcribe_dna_to_rna(dna_sequence):
    rna_sequence = ''
    for base in dna_sequence:
        rna_sequence += dna_to_rna.get(base, '')
    return rna_sequence

def translate_rna_to_protein(rna_sequence):
    protein_sequence = ''
    for i in range(0, len(rna_sequence), 3):
        codon = rna_sequence[i:i+3]
        amino_acid = rna_to_amino_acid.get(codon, 'X')  # Use 'X' if codon is not found
        protein_sequence += amino_acid + ' '
    return protein_sequence

# DNA sequence to transcribe and translate to protein
dna_sequence = 'ATGCTAGCGTACCGTACTAG'
rna_sequence = transcribe_dna_to_rna(dna_sequence)
protein_sequence = translate_rna_to_protein(rna_sequence)

print('DNA Sequence:', dna_sequence)
print('RNA Sequence:', rna_sequence)
print('Amino Acid Sequence:', protein_sequence)





