from collections import Counter

# Läs in filen och bearbeta DNA-sekvenser
with open("C:/Users/tobyh/Documents/CodingProjects/python_tobyhatrick_opa24/dna_raw.txt", "r") as file:
    data = file.read().splitlines()

for i in range(0, len(data), 2):  # hoppar över varje två rader (ID och sekvens)
    seq_id = data[i]
    sequence = data[i+1].upper()
    counts = Counter(sequence)
    print(f"{seq_id}: {dict(counts)}")