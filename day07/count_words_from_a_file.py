import sys
from collections import Counter

file = sys.argv[1]

with open(file, 'r') as document:
    content = document.read()

words = content.split()
counts = Counter(words)

for word, count in sorted(counts.items()):  
    print(f"{word}: {count}")             