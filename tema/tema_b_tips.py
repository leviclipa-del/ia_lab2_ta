import pandas as pd
import seaborn as sns

# Incarcare dataset
tips = sns.load_dataset('tips')

# 1. Dimensiune, tipuri de date si statistici descriptive
print("=== Informatii generale ===")
print(f"Dimensiune: {tips.shape}")
print(f"\nTipuri de date:\n{tips.dtypes}")
print(f"\nStatistici descriptive:\n{tips.describe()}")

# 2. Bacsisul mediu per zi si per sex
print("\n=== Bacsis mediu per zi ===")
print(tips.groupby('day', observed=True).mean(numeric_only=True)['tip'])

print("\n=== Bacsis mediu per sex ===")
print(tips.groupby('sex', observed=True).mean(numeric_only=True)['tip'])

# 3. Creare coloana noua procent_bacsis
tips_copie = tips.copy()
tips_copie['procent_bacsis'] = (tips_copie['tip'] / tips_copie['total_bill']) * 100

# 4. Cele mai generoase 5 mese
print("\n=== Cele mai generoase 5 mese ===")
top_5_mese = tips_copie.sort_values(by='procent_bacsis', ascending=False).head(5)
print(top_5_mese[['total_bill', 'tip', 'procent_bacsis']])

# 5. Cate mese au fost servite per zi si per categorie de fumatori
print("\n=== Numar mese per zi si per categorie fumatori ===")
numar_mese = tips.groupby(['day', 'smoker'], observed=True).size()
print(numar_mese)