# Restaurant Analytics Dashboard & Live SQL Runner

Dashboard interactif d'analyse de données et explorateur SQL en direct, développé avec **Python**, **SQLite** et **Streamlit**.

Ce projet démontre la mise en place d'un pipeline complet : de l'ingestion de données brutes jusqu'à la restitution visuelle de KPIs métier et l'exécution interactive de requêtes analytiques.

---

##  Fonctionnalités

- **Pipeline de données complet** : Ingestion d'un jeu de données brut (`tips.csv`), modélisation et stockage dans une base relationnelle locale **SQLite**.
- **Indicateurs clés (KPIs)** : Calcul en temps réel du Chiffre d'Affaires total, du cumul des pourboires, du taux de pourboire moyen et du volume de tables servies.
- **Visualisations & Analyses** : Distribution du chiffre d'affaires par jour de la semaine via **Matplotlib** et tableaux interactifs.
- **Explorateur SQL en direct** : Interface de bac à sable permettant d'exécuter des requêtes SQL personnalisées sur la base avec sécurisation en lecture seule (`SELECT`).

---

## 🛠️ Stack Technique

- **Langage** : Python 3
- **Base de données** : SQLite3
- **Manipulation de données** : Pandas
- **Dashboard & Interface** : Streamlit
- **Visualisation** : Matplotlib / Seaborn

---

##  Installation et Lancement

1. **Cloner le dépôt :**
   \`\`\`bash
   git clone https://github.com/<TON_PSEUDO>/projet1_sql_dashboard.git
   cd projet1_sql_dashboard
   \`\`\`

2. **Créer et activer l'environnement virtuel :**
   \`\`\`bash
   python -m venv venv
   # Sur Windows :
   venv\Scripts\activate
   \`\`\`

3. **Installer les dépendances :**
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

4. **Initialiser la base de données :**
   \`\`\`bash
   python db_setup.py
   \`\`\`

5. **Lancer le dashboard Streamlit :**
   \`\`\`bash
   streamlit run app.py
   \`\`\`

---

##  Structure du Projet

\`\`\`text
projet1_sql_dashboard/
├── data/
│   └── tips.csv         # Données sources
├── app.py               # Application web Streamlit
├── db_setup.py          # Script d'ingestion et création SQLite
├── get_data.py          # Extraction initiale des données
├── queries.sql          # Requêtes analytiques documentées
├── requirements.txt     # Dépendances du projet
└── README.md
\`\`\`
