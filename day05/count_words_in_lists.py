celestial_objects = [
    'Moon', 'Gas', 'Asteroid', 'Dwarf', 'Asteroid', 'Moon', 'Asteroid'
]

count = {}

for word in celestial_objects:
    if word in count:
        count[word] += 1

    else:
        count[word] = 1


for word, count in count.items():
    print(f" {word} {count}")