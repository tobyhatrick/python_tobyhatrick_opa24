import pandas as pd  # Importerar pandas-biblioteket för att hantera och bearbeta data
import matplotlib.pyplot as plt  # Importerar matplotlib för att kunna skapa graferna
import os  # Hanterar filsystem och mappar

# Läser in Excel-filen som innehåller statistik för nationella prov
file_path = "riket2023_åk9_np.xlsx"

# Lista över ämnen som ska läsas in
subjects = ["Engelska", "Matematik", "Svenska", "Svenska som andraspråk"]
dataframes = {}  # Dictionary för att spara varje ämnes data

# Loopar genom varje ämne och läser in datan
for subject in subjects:
    # Läs in data från Excel-filen och hoppa över de första 6 raderna
    df = pd.read_excel(file_path, sheet_name=subject, skiprows=6, header=0)

    # Sätt nya kolumnnamn för att matcha uppgiften och göra tabellen mer läsbar
    df.columns = [
        "Plats", "Huvudman", "Totalt (A-F)", "Flickor (A-F)", "Pojkar (A-F)", 
        "Totalt (A-E)", "Flickor (A-E)", "Pojkar (A-E)", 
        "Totalt (poäng)", "Flickor (poäng)", "Pojkar (poäng)"
    ]

    # Ta bort rader där "Plats" eller "Huvudman" saknar värden
    df = df.dropna(subset=["Plats", "Huvudman"])

    # Konvertera kolumnen "Huvudman" till strängar och ta bort decimaler (t.ex. "1.0" blir "1")
    df["Huvudman"] = df["Huvudman"].astype(str).replace(r'\.0$', '', regex=True)

    # Ta bort rader där "Huvudman" är tom eller innehåller "nan"
    df = df[df["Huvudman"].str.strip() != ""]  # Ta bort tomma strängar
    df = df[df["Huvudman"].str.lower() != "nan"]  # Ta bort "nan"

    # Ta bort rader där "Huvudman" innehåller rubriker (t.ex. "Typ av huvudman")
    df = df[~df["Huvudman"].str.contains("Typ av huvudman", case=False)]

    # Återställ index för att hålla datan ren
    df.reset_index(drop=True, inplace=True)
    dataframes[subject] = df

# Skriver ut de första raderna av varje ämne
for subject, df in dataframes.items():
    print(f"Förhandsgranskning av {subject}:")
    print(df.head())  # Skriver ut de första 5 raderna för varje ämne

# Skapat en stapelgraf för totala poäng per huvudman
# Se till att mappen visualiseringar finns
os.makedirs("visualiseringar", exist_ok=True)

# Skapar en stapelgraf för varje ämne
for subject, df in dataframes.items():
    plt.figure(figsize=(8, 5))
    plt.bar(df["Huvudman"], df["Totalt (poäng)"], color=['blue', 'green', 'red', 'purple'])

    # Lägg till etiketter och titel
    plt.xlabel("Huvudman")
    plt.ylabel("Totalt (poäng)")
    plt.title(f"Totala poäng per huvudman - {subject}")

    # Rotera x-axelns etiketter för bättre läsbarhet
    plt.xticks(rotation=45, ha="right")

    # Spara grafen i undermappen visualiseringar
    plt.tight_layout()
    plt.savefig(f"visualiseringar/totala_poäng_{subject}.png")

    # Visa grafen
    plt.show()

# Skapar en subplot-graf för varje ämne
for subject, df in dataframes.items():
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    # Lista med kategorier och färger
    categories = ["Totalt (poäng)", "Flickor (poäng)", "Pojkar (poäng)"]
    colors = ["green", "red", "blue"]

    # Loopar igenom kategorierna och ritar upp stapeldiagram
    for i, category in enumerate(categories):
        axes[i].bar(df["Huvudman"], df[category], color=colors[i])  # Stapeldiagram
        axes[i].set_title(f"{category} - {subject}")  # Titel för subplot
        axes[i].set_xlabel("Huvudman")  # X-axel etikett
        axes[i].set_ylabel("Poäng")  # Y-axel etikett
        axes[i].tick_params(axis="x", rotation=45)  # Rotera x-etiketter för bättre läsbarhet

    # Lagt till en huvudtitel för hela figuren
    plt.suptitle(f"Poängfördelning per huvudman - {subject}", fontsize=14)

    # Justerat layout så att allt ser bra ut
    plt.tight_layout(rect=[0, 0, 1, 0.95])

    # Sparat figuren i visualiseringsmappen
    plt.savefig(f"visualiseringar/poängfördelning_{subject}.png")

    # Visar diagrammet
    plt.show()