import pandas as pd
import seaborn as sns

# incarcare dataset
iris = sns.load_dataset('iris')

# --- Explorare generala ---
print("=== Primele 5 inregistrari ===")
print(iris.head())

print("\n=== Informatii generale ===")
print(f"Dimensiune: {iris.shape[0]} linii x {iris.shape[1]} coloane")
print(f"Coloane: {iris.columns.tolist()}")
print(f"\nTipuri de date:\n{iris.dtypes}")
print(f"\nValori lipsa: \n{iris.isnull().sum()}")

print("\n=== Statistici descriptive ===")
print(iris.describe().round(2))

# distribuția speciilor 
print("\n=== Distributia speciilor ===")
print(iris['species'].value_counts())

# filtrare 
print("\n=== Flori Setosa cu lungimea sepalei > 5 cm ===")
setosa_mare = iris.loc[(iris['species'] == 'setosa') & (iris['sepal_length'] > 5.0)]
print(f"Numar inregistrari: {len(setosa_mare)}")
print(setosa_mare.head())

# gregare: medie per specie 
print("\n=== Medie per specie ===")
medie_per_specie = iris.groupby('species').mean(numeric_only=True).round(2)
print(medie_per_specie)

# adaugare coloana calculata 
iris_extins = iris.copy()
iris_extins['raport_petala'] = (iris_extins['petal_length'] / iris_extins['petal_width']).round(2)
print("\n=== Raport lungime/latime petala (primele 5) ===")
print(iris_extins[['species', 'petal_length', 'petal_width', 'raport_petala']].head())