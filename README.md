# F7 : Détection d'anomalies sur le S&P 500

**Auteur :** WAHHABI Zakaria · Code Apogée 23009144 · Groupe G3 · S7 Finance · ENCG Settat
**Cours :** BD & DS · Examen individuel, partie B

## Résumé

Un Isolation Forest est entraîné sur les rendements et la volatilité du S&P 500 de 2016 à 2021, puis appliqué à 2022-2026.
Il ne détecte aucune journée atypique sur le test, alors que la règle des 3 écarts-types en trouve 10, dont 80 % liées à des événements documentés.
Le modèle a appris une « normalité » qui contient le krach du Covid : les chocs plus modérés qui suivent passent sous son seuil.

## Problématique et résultats

**Question :** un Isolation Forest entraîné sur 2016-2021 repère-t-il, sur 2022-2026, des journées atypiques liées à des événements documentés, mieux qu'une règle des trois écarts-types ?

**Objectif (fixé avant le test) :** précision événementielle au moins 2 fois le niveau du hasard et au moins égale à celle de la référence. **Résultat : objectif non atteint.**

| Méthode | Période | Jours détectés | Précision événementielle | Niveau du hasard |
|---|---|---|---|---|
| Isolation Forest | Validation 2020-2021 | 31 | 96,8 % | 11,1 % |
| Référence (3 écarts-types) | Test 2022-2026 | 10 | 80,0 % | 6,2 % |
| Isolation Forest | Test 2022-2026 | 0 | — | 6,2 % |

## Données

- **Source :** S&P Dow Jones Indices LLC, S&P 500 [SP500], via FRED (Federal Reserve Bank of St. Louis)
- **Lien :** https://fred.stlouisfed.org/series/SP500
- **Période :** 7 novembre 2016 → 5 novembre 2026, quotidienne · **Date d'extraction :** [à compléter]
- **Licence :** la reproduction de la série est interdite sans autorisation écrite de S&P Dow Jones Indices. Le fichier n'est donc **pas** déposé ici : voir `data/raw/LISEZMOI.md` et `src/telecharger_donnees.py`.

## Installation

Python 3.10 ou plus récent (testé avec Python 3.13 sur Google Colab).

```bash
pip install -r requirements.txt
```

## Exécution

1. Télécharger les données : `python src/telecharger_donnees.py` (ou manuellement, voir `data/raw/LISEZMOI.md`).
2. Ouvrir `notebooks/projet_F7.ipynb`, adapter le chemin `FICHIER` dans la configuration (sur Colab, le notebook lit le fichier depuis Google Drive, méthode validée par l'enseignant), puis « Redémarrer et tout exécuter ».
3. Durée : moins de 2 minutes. Les graphiques sont enregistrés dans `figures/`.

## Structure du dépôt

```
23009144-WAHHABI-G3/
├── README.md
├── requirements.txt
├── .gitignore
├── DECLARATION_IA.md
├── data/
│   ├── raw/LISEZMOI.md          # comment obtenir les données (licence)
│   └── processed/
├── docs/
│   ├── fiche_sujet_F7.md
│   └── references.md
├── notebooks/projet_F7.ipynb    # notebook final exécuté
├── src/telecharger_donnees.py
├── figures/                     # 8 graphiques
├── rapport/rapport.pdf          # export PDF du notebook
└── presentation/                # 6 diapositives (PDF et PPTX)
```

## Références

Voir `docs/references.md`. Utilisation d'outils d'IA : voir `DECLARATION_IA.md`.
