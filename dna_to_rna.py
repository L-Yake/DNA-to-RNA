"""
Translate DNA to RNA using Python Strings

Reference: https://www.codewars.com/kata/5556282156230d0e5e000089/train/python
"""


def dna_to_rna(dna):
    """
    DNA is composed of Guanine ('G'), Cytosine ('C'), Adenine ('A'), and Thymine ('T')
    RNA is composed of the same except for Thymine('T') which is replaced by Uracil ('U')

    Example 1:
        dna_proteins = 'TTTT'
        dna_to_rna(dna_proteins)
    >>> 'UUUU'

    Example 2:
        dna_proteins = 'GCAT'
        dna_to_rna(dna_proteins)
    >>> 'GCAU'
    """
    return dna.replace('T', 'U')


