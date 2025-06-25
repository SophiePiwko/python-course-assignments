import os
from collections import defaultdict

codon_table = {
    'Phe': ['TTT', 'TTC'],
    'Leu': ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'],
    'Ile': ['ATT', 'ATC', 'ATA'],
    'Met': ['ATG'],
    'Val': ['GTT', 'GTC', 'GTA', 'GTG'],
    'Ser': ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'],
    'Pro': ['CCT', 'CCC', 'CCA', 'CCG'],
    'Thr': ['ACT', 'ACC', 'ACA', 'ACG'],
    'Ala': ['GCT', 'GCC', 'GCA', 'GCG'],
    'Tyr': ['TAT', 'TAC'],
    'His': ['CAT', 'CAC'],
    'Gln': ['CAA', 'CAG'],
    'Asn': ['AAT', 'AAC'],
    'Lys': ['AAA', 'AAG'],
    'Asp': ['GAT', 'GAC'],
    'Glu': ['GAA', 'GAG'],
    'Cys': ['TGT', 'TGC'],
    'Trp': ['TGG'],
    'Arg': ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
    'Gly': ['GGT', 'GGC', 'GGA', 'GGG'],
    'STOP': ['TAA', 'TAG', 'TGA']
}

codon_to_amino = {}
for amino, codons in codon_table.items():
    for codon in codons:
        codon_to_amino[codon] = amino

def show_usage():
    print("\nUsage: python count_amino_acids.py path/to/dna_sequence.txt")
    print("Example: python count_amino_acids.py examples/dna.txt\n")   


def read_sequence_from_file(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            sequence = ''.join(line.strip() for line in lines if not line.startswith('>'))
            sequence = ''.join([base for base in sequence.upper() if base in "ACTG"])
            return sequence
    except FileNotFoundError:
        print(f"Error: File '{path}' not found. ")
        show_usage()
        exit(1)
    except Exception as e:
        print(f"An error occured while reading the file: {e}")
        exit(1)
    
def count_amino_acids(sequence):
    counts = defaultdict(int)
    stop_codons = 0

    for i in range(0, len(sequence) -2,3):
        codon - sequence[i:i+3]
        amino = codon_to_amino.get(codon)

        if not amino:
            continue
        if amino == 'STOP':
            stop_codons += 1
            continue
        counts[amino] += 1

    return counts, stop_codons

def display_results(counts, stop_codons):
    print("\nAmino Acid Frequence:")
    for amino, count in sorted(counts.items()):
        print(f"{amino}: {count}")
    print(f"\nSTOP codons encounteres (ignored): {stop_codons}")