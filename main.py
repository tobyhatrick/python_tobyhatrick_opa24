from collections import Counter

# Läs in filen och bearbeta DNA-sekvenser
with open("C:/Users/tobyh/Documents/CodingProjects/python_tobyhatrick_opa24/dna_raw.txt", "r") as file:
    data = file.read().split("\n>")  # Dela upp sekvenser vid varje ">"