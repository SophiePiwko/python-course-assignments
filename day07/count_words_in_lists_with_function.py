celestial_objects = [
    'Moon', 'Gas', 'Asteroid', 'Dwarf', 'Asteroid', 'Moon', 'Asteroid'
]

import sys
from collections import Counter
import os

def show_usage():

    script = os.path.basename(sys.argv[0])
    print(f"\nUsage: python {script} path/to/textfile.txt")
    print("Example: python count_words_from_a_file.py examples/dictionary/words_and_spaces.txt\n")

def read_file_content(filepath):

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        show_usage()
        sys.exit(1)
    except Exception as e:
        print(f"Error while reading the file: {e}")
        sys.exit(1)

def count_words(text):

    words = text.lower().split()
    return Counter(words)

def results(counter):

    print("\nWord Frequency Count:")
    for word, count in counter.most_common():
        print(f"{word}: {count}")

def main():
    if len(sys.argv) != 2:
        print("Error: You must provide exactly one file path as argument.")
        show_usage()
        sys.exit(1)

    filepath = sys.argv[1]
    text = read_file_content(filepath)
    word_counts = count_words(text)
    display_results(word_counts)

if __name__ == '__main__':
    main()