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

