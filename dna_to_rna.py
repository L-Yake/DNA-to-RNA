"""
Translate DNA to RNA using Python Strings

Reference: https://www.codewars.com/kata/5556282156230d0e5e000089/train/python
"""

proteins = 'TTTT'
protein2 = 'GCAT'

def dna_to_rna(dna):
    """
    DNA is composed of Guanine ('G'), Cytosine ('C'), Adenine ('A'), and Thymine ('T')
    RNA is composed of the same except for Thymine('T') which is replaced by Uracil ('U')

    Example:
        proteins = 'TTTT'
        dna_to_rna(proteins)

        >>> 'UUUU'
    """
    # Empty RNA string
    rna = ''
    # Check each piece of information in DNA for Thymine('T')
    for piece in dna:
        # If piece is Thymine('T') convert to Uracil('U')
        if piece == 'T':
            # Add piece onto RNA
            rna += 'U'
        else:
            rna += piece


dna_to_rna(protein2)