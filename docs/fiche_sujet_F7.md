# F7. Anomalies sur le S&P 500

*Fiche extraite de `projets_finance_science_donnees.md`.*

- **Question :** quelles journées de marché sont statistiquement atypiques, et correspondent-elles à des événements connus ?
- **Tâche :** détection d'anomalies sans étiquettes.
- **Données :** FRED SP500, https://fred.stlouisfed.org/graph/fredgraph.csv?id=SP500. Environ 2 500 observations quotidiennes depuis 2016.
- **Prétraitement :** calculer les rendements logarithmiques et la volatilité glissante sur 20 jours.
- **Modèles :** Isolation Forest, LOF.
- **Métriques :** proportion d'anomalies détectées, comparaison qualitative avec des événements documentés.
- **Livrable :** notebook et frise chronologique des anomalies.
- **Risque :** sans étiquettes, l'évaluation reste subjective. Le signaler clairement.

**Précisions de l'énoncé de l'examen (CC partie B) :** algorithme principal n° 24 (Isolation Forest), 19 ou 20 possibles ; LOF n'est pas dans le support, comparaison facultative seulement. Référence naïve : observation à plus de trois écarts-types de la moyenne.
