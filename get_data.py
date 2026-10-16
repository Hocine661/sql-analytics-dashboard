import seaborn as sns
import os
os.makedirs('data', exist_ok=True)
df = sns.load_dataset('tips')
df.to_csv('data/tips.csv', index=False)
print(f"{len(df)} lignes récupérées → data/tips.csv")