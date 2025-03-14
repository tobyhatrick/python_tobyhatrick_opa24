import plotly.express as px
import pandas as pd
import os

# Skapa mappen visualiseringar om den inte finns
os.makedirs("visualiseringar", exist_ok=True)

# ------------------------------------------
# Uppgift 2a: Andel elever utan godkänt betyg
# ------------------------------------------

def uppgift_2a():
    # Läser in Excel-filen med betygsdata
    header_row = 7  # Radnumret där kolumnrubrikerna börjar
    df = pd.read_excel("betyg_o_prov_riksnivå.xlsx", sheet_name="Tabell 1B", engine="openpyxl", header=header_row)

    # Byt namn på första kolumnen till läsår
    df.rename(columns={"Unnamed: 0": "Läsår"}, inplace=True)

    # Filtrera ut endast läsår 2018/19 – 2022/23
    df = df[df["Läsår"].astype(str).str.match(r"^\d{4}/\d{2}$")]  # Filtrerar ut rader där Läsår är skrivet som YYYY/YY

    # Bytt namn på relevanta kolumner för andel elever utan godkänt betyg
    df.rename(columns={
        "Totalt.2": "Totalt (%)",  # Kolumnen för totalt saknar godkänt
        "Flickor.2": "Flickor (%)",  # Kolumnen för flickor saknar godkänt
        "Pojkar.2": "Pojkar (%)"  # Kolumnen för pojkar saknar godkänt
    }, inplace=True)

    # Kontrollera att de valda kolumnerna finns i DataFrame, annars stoppa programmet
    förlorade_kolumner = [kol for kol in ["Totalt (%)", "Flickor (%)", "Pojkar (%)"] if kol not in df.columns]
    if förlorade_kolumner:
        raise ValueError(f"Följande kolumner saknas: {förlorade_kolumner}")

    # Skapar ett linjediagram med plotly express
    fig = px.line(
        df,
        x="Läsår",  # X-axeln visar olika läsår 2018/19 - 2022/23
        y=["Totalt (%)", "Flickor (%)", "Pojkar (%)"],  # Y-axeln visar andel elever utan godkänt betyg
        markers=True,  # Lägger till punkter på linjerna för att tydliggöra värdena
        title="Andel elever utan godkänt betyg (2018-2023)",  # Titel för diagrammet
        labels={"value": "Andel elever (%)", "variable": "Kön", "Läsår": "Läsår"}  # Anpassar etiketter
    )

    # Anpassar utseendet på grafen
    fig.update_traces(line=dict(width=3), marker=dict(size=8))  # Gör linjerna tjockare (3 px) och förstorar markörerna (8 px)
    fig.update_yaxes(title_text="Andel elever utan godkänt betyg (%)")  # Sätter en tydlig titel på y-axeln
    fig.update_xaxes(title_text="Läsår")  # Sätter en tydlig titel på x-axeln

    # Sparar filen i mappen visualiseringar
    html_path = "visualiseringar/andel_elever_utan_godkänt.html"
    fig.write_html(html_path)

    print(f"Grafen har sparats som HTML: {html_path}")

    # Visa grafen i webbläsaren
    fig.show()

# ------------------------------------------
# Uppgift 2b: Genomsnittligt meritvärde för 16 ämnen
# ------------------------------------------

def uppgift_2b():
    # Läser in Excel-filen med betygsdata
    header_row = 7  # Radnumret där kolumnrubrikerna börjar
    df = pd.read_excel("betyg_o_prov_riksnivå.xlsx", sheet_name="Tabell 1B", engine="openpyxl", header=header_row)

    # Byt namn på första kolumnen till läsår
    df.rename(columns={"Unnamed: 0": "Läsår"}, inplace=True)

    # Filtrera ut endast läsår 2018/19 – 2022/23
    df = df[df["Läsår"].astype(str).str.match(r"^\d{4}/\d{2}$")]  # Filtrerar ut rader där Läsår är skrivet som YYYY/YY

    # Bytt namn på relevanta kolumner för genomsnittligt meritvärde för 16 ämnen
    df.rename(columns={
        "Totalt": "Totalt meritvärde",  # Kolumnen för totalt meritvärde
        "Flickor": "Flickor meritvärde",  # Kolumnen för flickor meritvärde
        "Pojkar": "Pojkar meritvärde"  # Kolumnen för pojkar meritvärde
    }, inplace=True)

    # Kontrollera att de valda kolumnerna finns i DataFrame, annars stoppa programmet
    förlorade_kolumner = [kol for kol in ["Totalt meritvärde", "Flickor meritvärde", "Pojkar meritvärde"] if kol not in df.columns]
    if förlorade_kolumner:
        raise ValueError(f"Följande kolumner saknas: {förlorade_kolumner}")

    # Skapar ett linjediagram med plotly express
    fig = px.line(
        df,
        x="Läsår",  # X-axeln visar olika läsår 2018/19 - 2022/23
        y=["Totalt meritvärde", "Flickor meritvärde", "Pojkar meritvärde"],  # Y-axeln visar genomsnittligt meritvärde
        markers=True,  # Lägger till punkter på linjerna för att tydliggöra värdena
        title="Genomsnittligt meritvärde för 16 ämnen (2018-2023)",  # Titel för diagrammet
        labels={"value": "Meritvärde", "variable": "Kön", "Läsår": "Läsår"}  # Anpassar etiketter
    )

    # Anpassar utseendet på grafen
    fig.update_traces(line=dict(width=3), marker=dict(size=8))  # Gör linjerna tjockare (3 px) och förstorar markörerna (8 px)
    fig.update_yaxes(title_text="Genomsnittligt meritvärde")  # Sätter en tydlig titel på y-axeln
    fig.update_xaxes(title_text="Läsår")  # Sätter en tydlig titel på x-axeln

    # Sparar filen i mappen visualiseringar
    html_path = "visualiseringar/meritvärde_16_ämnen.html"
    fig.write_html(html_path)

    print(f"Grafen har sparats som HTML: {html_path}")

    # Visa grafen i webbläsaren
    fig.show()

# Kör uppgifterna
uppgift_2a()
uppgift_2b()