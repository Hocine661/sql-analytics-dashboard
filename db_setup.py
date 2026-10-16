import sqlite3
import pandas as pd
df = pd.read_csv('data/tips.csv')
conn = sqlite3.connect('tips.db')
df.to_sql('tips', conn, if_exists='replace', index=False)
conn.close()

print("Succés !!!")
