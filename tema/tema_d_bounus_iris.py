import matplotlib.pyplot as plt
import seaborn as sns

iris = sns.load_dataset('iris')
sns.set_theme(style='ticks')

# 1. Pairplot complet
pairplot_fig = sns.pairplot(iris, hue='species', diag_kind='kde')
pairplot_fig.figure.suptitle('Analiza Pairplot - Dataset Iris', y=1.02, fontsize=16)
pairplot_fig.savefig('iris_pairplot.png', dpi=150, bbox_inches='tight')
plt.show()

# 2. Figura separata cu 4 subploturi (Violinplots)
fig, axes = plt.subplots(1, 4, figsize=(20, 6))
fig.suptitle('Distributia variabilelor numerice pe specii (Violinplots)', fontsize=16, fontweight='bold')

variabile = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
titluri = ['Lungime Sepala', 'Latime Sepala', 'Lungime Petala', 'Latime Petala']

for i in range(4):
    sns.violinplot(data=iris, x='species', y=variabile[i], hue='species', split=False, ax=axes[i], legend=False)
    axes[i].set_title(titluri[i])
    axes[i].set_xlabel('Specie')
    axes[i].set_ylabel('Dimensiune (cm)')

plt.tight_layout()
plt.savefig('iris_violinplots.png', dpi=150, bbox_inches='tight')
plt.show()