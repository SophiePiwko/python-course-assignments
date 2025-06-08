import sys
import os
from collections import defaultdict

codon_table = {
    'Phe' : ['TTT', 'TTC'],
    'Leu' : ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'],
    'Ile' : ['ATT', 'ATC', 'ATA'],
    'Met' : ['ATG'],
    'Val' : ['GTT', 'GTC', 'GTA', 'GTG'],
    'Ser' : ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'],
    'Pro' : ['CCT', 'CCC', 'CCA', 'CCG'],
    'Thr' : ['ACT', 'ACC', 'ACA', 'ACG'],
    'Ala' : ['GCT', 'GCC', 'GCA', 'GCG'],
    'Tyr' : ['TAT', 'TAC'],
    'His' : ['CAT', 'CAC'],
    'Gln' : ['CAA', 'CAG'],
    'Asn' : ['AAT', 'AAC'],
    'Lys' : ['AAA', 'AAG'],
    'Asp' : ['GAT', 'GAC'],
    'Glu' : ['GAA', 'GAG'],
    'Cys' : ['TGT', 'TGC'],
    'Trp' : ['TGG'],
    'Arg' : ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
    'Gly' : ['GGT', 'GGC', 'GGA', 'GGG'],
    'STOP' : ['TAA', 'TAG', 'TGA']
}

codon_to_amino = {}
for amino, codons in codon_table.items():
    for codon in codons:
        codon_to_amino[codon] = amino

def show_usage():
    script = os.path.basename(sys.argv[0])
    print(f"\nUsage: python {script} path/to/dna_sequence.txt")
    print("Example: count_amino_acids.py examples/dna.txt\n")

def read_sequence_from_file(path):
    try:
        with open(path, 'r', encoding = 'utf-8') as f:
            lines = f.readlines()
            sequence = ''.join(line.strip() for line in lines if not line.startswith('>'))
            sequence = ''.join([base for base in sequence.upper() if base in "ACTG"])
            return sequence
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
        show_usage()
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        sys.exit(1)

def count_amino_acids(sequence):
    counts = defaultdict(int)
    stop_codons = 0
    for i in range(0, len(sequence) - 2, 3):
        codon = sequence[i:i+3]
        amino = codon_to_amino.get(codon)
        if not amino:
            continue  # Skip invalid codons
        if amino == 'STOP':
            stop_codons += 1
            continue
        counts[amino] += 1
    return counts, stop_codons

def display_results(counts, stop_codons):
    print("n\Amino Acid Frequence:")
    for amino, count in sorted(counts.items()):
        print(f"{amino}: {count}")
    print(f"\nSTOP codons found (ignored): {stop_codons}")

def main():
    if len(sys.argv) != 2:
        print("Error: Please provide exactly one path to a DNA sequence file.")
        show_usage()
        sys.exit(1)

    filepath = sys.argv[1]
    dna_sequence = read_sequence_from_file(filepath)
    if len(dna_sequence) < 3:
        print("Error: DNA sequence is too short to form codons.")
        sys.exit(1)

    amino_counts, stop_count = count_amino_acids(dna_sequence)
    display_results(amino_counts, stop_count)

if __name__ == '__main__':
    main()