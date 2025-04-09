import matplotlib.pyplot as plt

# Läs in DNA-fil
def read_dna_file(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
    
    sequences = {}
    current_id = ""
    
    # Bearbeta varje rad i filen
    for line in lines:
        line = line.strip()
        if line.startswith(">"):  # Identifier
            current_id = line[1:]
            sequences[current_id] = ""
        else:  # DNA-sekvens
            sequences[current_id] += line.lower()  # Gör sekvensen case-insensitive
    
    return sequences

# Räkna baser i DNA-sekvensen
def count_dna_bases(sequence):
    dna_count = {"a": 0, "t": 0, "c": 0, "g": 0}
    for letter in sequence:
        if letter in dna_count:
            dna_count[letter] += 1
    return dna_count

