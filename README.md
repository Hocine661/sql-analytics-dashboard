# Dashboard d'Analyse de Données & Explorateur SQL Self-Service

**Pipeline Data & Application BI Interactive** développés avec **Python**, **SQLite**, **Pandas** et **Streamlit**.

Ce projet présente une architecture modulaire de **Data Visualisation & Self-Service BI**. Bien qu'illustré ici sur un jeu de données transactionnel de restauration (`tips`), le pipeline a été conçu de manière **générique et réutilisable** pour s'adapter à tout type de données métiers (suivi RH, indicateurs d'activité, finance, ventes).

---

## Objectifs du Projet

1. **Automatiser l'ingestion et la fiabilisation** : Transformer des fichiers plats (`.csv`) en une base de données relationnelle structurée (`SQLite`).
2. **Aide à la décision (KPIs)** : Concevoir des requêtes SQL analytiques (agrégations, ratios, groupements) pour restituer des indicateurs clés de performance fiables.
3. **Self-Service Data & Accompagnement métier** : Offrir aux utilisateurs finaux un **explorateur SQL en direct** sécurisé, leur permettant d'interroger la base en autonomie sans risque d'altération des données.

---

## Fonctionnalités Clés

- **Pipeline ETL léger (`get_data.py` & `db_setup.py`)** : Extraction automatisée, nettoyage via Pandas et chargement en base relationnelle SQLite.
- **Tableau de bord de suivi de KPIs (`app.py`)** :
  - Cartes d'indicateurs synthétiques (Chiffre d'affaires, volumes, ratios moyens).
  - Visualisation graphique de la répartition d'activité (Matplotlib) couplée aux tables d'agrégation.
- **Explorateur SQL en direct (Mode Self-Service)** :
  - Exécution de requêtes SQL personnalisées à la volée avec retour immédiat sous forme de DataFrame interactif.
  - **Sécurité & Gouvernance** : Filtrage préventif bloquant les instructions destructrices (`DROP`, `DELETE`, `UPDATE`, `INSERT`, `ALTER`) afin de garantir un accès strictement en lecture seule (`SELECT`).

---

## Architecture Modulaire & Transposabilité Métier

L'architecture sépare strictement la couche de données, le requêtage analytique et le rendu visuel. Pour transposer ce dashboard à un autre contexte métier (ex: **Reporting RH, suivi d'incidents IT, contrôle de gestion**) :

1. **Source** : Remplacer le fichier CSV source dans `data/`.
2. **Ingestion** : Relancer `db_setup.py` pour générer automatiquement le nouveau schéma SQLite.
3. **Analytique** : Adapter les règles de gestion et KPIs dans `queries.sql` et `app.py`.

```text
sql-analytics-dashboard/
├── data/
│   └── tips.csv          # Données sources (remplaçable par tout export métier CSV)
├── get_data.py           # Script de récupération / extraction des données
├── db_setup.py           # Pipeline d'ingestion CSV -> Base relationnelle SQLite
├── queries.sql           # Bibliothèque de requêtes SQL analytiques testées
├── app.py                # Interface Streamlit (Visualisation KPIs & Live SQL Runner)
├── requirements.txt      # Dépendances Python
└── README.md             # Documentation technique
\`\`\`
