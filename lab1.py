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

# Rita graf över frekvenser av DNA-baser
def plot_dna_frequencies(dna_count, sequence_id):
    letters = list(dna_count.keys())
    values = list(dna_count.values())
    
    # Skapa stapeldiagram
    plt.bar(letters, values, color=["blue", "red", "green", "orange"])
    plt.xlabel("DNA Baser")
    plt.ylabel("Frekvens")
    plt.title(f"Frekvens av DNA-baser - {sequence_id}")
    plt.show()

# Huvudfunktion
def main():
    filename = "dna_raw.txt"  # Filnamn
    sequences = read_dna_file(filename)  # Läs in sekvenser från fil
    
    # Bearbeta varje sekvens
    for seq_id, sequence in sequences.items():
        dna_count = count_dna_bases(sequence)  # Räkna baserna
        print(f"{seq_id}: {dna_count}")
        plot_dna_frequencies(dna_count, seq_id)  # Rita graf för varje sekvens

# Kör programmet
if __name__ == "__main__":
    main()