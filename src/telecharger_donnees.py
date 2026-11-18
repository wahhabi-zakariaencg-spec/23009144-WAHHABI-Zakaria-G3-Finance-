"""Télécharge la série S&P 500 depuis FRED dans data/raw/SP500.csv."""
from datetime import date
from pathlib import Path

import pandas as pd

URL = "https://fred.stlouisfed.org/graph/fredgraph.csv?id=SP500"
DESTINATION = Path(__file__).resolve().parent.parent / "data" / "raw" / "SP500.csv"

if __name__ == "__main__":
    donnees = pd.read_csv(URL)
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    donnees.to_csv(DESTINATION, index=False)
    print(f"{len(donnees)} lignes enregistrées dans {DESTINATION} (extraction du {date.today()})")
