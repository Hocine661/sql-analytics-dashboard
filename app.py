import sqlite3
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Configuration de la page
st.set_page_config(page_title="Dashboard Tips Analytics", layout="wide")
st.title("Dashboard d'Analyse des Données Restauration")

# Connexion à la base SQLite
conn = sqlite3.connect("tips.db")

# Onglets principaux
tab1, tab2 = st.tabs(["📈 Vue d'ensemble & KPIs", "💻 Explorateur SQL en direct"])

# ----------------- ONGLET 1 : KPIS & VISUALISATIONS -----------------
with tab1:
    # 1. Requête des KPIs globaux
    kpi_query = """
    SELECT 
        ROUND(SUM(total_bill), 2) AS ca_total,
        ROUND(SUM(tip), 2) AS pourboires_total,
        ROUND(AVG((tip / total_bill) * 100), 2) AS pct_tip_moyen,
        COUNT(*) AS total_tables
    FROM tips;
    """
    df_kpi = pd.read_sql_query(kpi_query, conn)

    # Affichage des cartes de métriques
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Chiffre d'Affaires", f"{df_kpi['ca_total'][0]} $")
    col2.metric("Total Pourboires", f"{df_kpi['pourboires_total'][0]} $")
    col3.metric("Taux de Pourboire Moyen", f"{df_kpi['pct_tip_moyen'][0]} %")
    col4.metric("Couverts / Tables", int(df_kpi['total_tables'][0]))

    st.divider()

    # 2. Graphique : Chiffre d'affaires par jour
    day_query = """
    SELECT day, ROUND(SUM(total_bill), 2) AS ca_total
    FROM tips
    GROUP BY day
    ORDER BY ca_total DESC;
    """
    df_day = pd.read_sql_query(day_query, conn)

    col_graph1, col_graph2 = st.columns(2)

    with col_graph1:
        st.subheader("Chiffre d'affaires par jour")
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.bar(df_day["day"], df_day["ca_total"], color="#4CAF50")
        ax.set_ylabel("CA ($)")
        st.pyplot(fig)

    with col_graph2:
        st.subheader("Données brutes agrégées")
        st.dataframe(df_day, use_container_width=True)

# ----------------- ONGLET 2 : EXPLORATEUR SQL -----------------
with tab2:
    st.subheader("Exécute ta propre requête SQL sur `tips.db`")
    default_query = "SELECT day, time, AVG(tip) AS avg_tip FROM tips GROUP BY day, time;"
    user_query = st.text_area("Requête SQL :", value=default_query, height=120)

    if st.button("Lancer la requête"):
        # Sécurité basique en lecture seule
        forbidden_keywords = ["DROP", "DELETE", "UPDATE", "INSERT", "ALTER"]
        if any(word in user_query.upper() for word in forbidden_keywords):
            st.error("Action interdite : seules les requêtes de lecture (SELECT) sont autorisées.")
        else:
            try:
                res = pd.read_sql_query(user_query, conn)
                st.success(f"{len(res)} lignes retournées")
                st.dataframe(res, use_container_width=True)
            except Exception as e:
                st.error(f"Erreur SQL : {e}")

conn.close()