import sys

def valid_sequence(sequence):
    bases = "ACTG"
    base_sequence = []
    current = ""

    for char in sequence:
        if char.isalpha() and char in bases:
            current += char

        elif char == 'X':
            base_sequence.append(current)
            current = ""

    if current:
        base_sequence.append(current)

    return base_sequence

def main():
    if len(sys.argv) != 2:
        print("Use python dna_sequencing.py <sequence>")
        sys.exit(1)

    sequence = sys.argv[1]

    base_sequence = valid_sequence(sequence)
    print(base_sequence)

    base_sequence.sort (key=len, reverse = True)

    print(base_sequence)

if __name__ == '__main__':
    main()