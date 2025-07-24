import sys
from amino_acid_counter import parse_fasta_sequence, translate_sequence, count_amino_acids

def main():
    if len(sys.argv) != 2:
        print("Usage: python count_amino_acids_with_module.py <fasta_file>")
        sys.exit(1)

    fasta_file = sys.argv[1]
    sequence, trimmed = parse_fasta_sequence(fasta_file)

    print(f"Old sequence length: {len(sequence)}")
    print(f"Trimmed sequence length: {len(trimmed)}")

    amino_acids = translate_sequence(trimmed)
    counts = count_amino_acids(amino_acids)

    print("----\nAmino Acid Counts:")
    for aa, count in counts.most_common():
        print(f"{aa}: {count}")

if __name__ == "__main__":
    main()
