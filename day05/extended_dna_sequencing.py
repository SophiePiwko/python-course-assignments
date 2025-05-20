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
    sequence = input("Please type in a sequence: ")
    base_sequence = valid_sequence(sequence)
    print(base_sequence)

    base_sequence.sort(key=len, reverse = True)
    print(base_sequence)

if __name__ == '__main__':
    main()