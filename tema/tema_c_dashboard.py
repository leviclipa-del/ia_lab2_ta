import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')
sns.set_theme(style='whitegrid')

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Dashboard Analiza Tips', fontsize=16, fontweight='bold')

# 1. Scatter (Matplotlib): total_bill vs. tip, colorat dupa sex
culori_sex = {'Male': '#3498db', 'Female': '#e74c3c'}
for sex, culoare in culori_sex.items():
    subset = tips[tips['sex'] == sex]
    axes[0, 0].scatter(subset['total_bill'], subset['tip'], label=sex, color=culoare, alpha=0.7)
axes[0, 0].set_title('Total Bill vs Tip')
axes[0, 0].set_xlabel('Total Bill ($)')
axes[0, 0].set_ylabel('Tip ($)')
axes[0, 0].legend(title='Sex')

# 2. Boxplot (Seaborn): distributia total_bill per day
sns.boxplot(data=tips, x='day', y='total_bill', order=['Thur', 'Fri', 'Sat', 'Sun'], ax=axes[0, 1])
axes[0, 1].set_title('Distributia notei de plata per zi')
axes[0, 1].set_xlabel('Ziua saptamanii')
axes[0, 1].set_ylabel('Total Bill ($)')

# 3. Histograma (Seaborn): distributia tip, cu hue='time' si KDE
sns.histplot(data=tips, x='tip', hue='time', kde=True, ax=axes[1, 0], bins=20)
axes[1, 0].set_title('Distributia bacsisurilor pe momentul zilei')
axes[1, 0].set_xlabel('Tip ($)')
axes[1, 0].set_ylabel('Frecventa')

# 4. Barplot (Seaborn): bacsisul mediu per day, order Thur->Sun
sns.barplot(data=tips, x='day', y='tip', order=['Thur', 'Fri', 'Sat', 'Sun'], errorbar='ci', ax=axes[1, 1], palette='Set2', hue='day', legend=False)
axes[1, 1].set_title('Bacsisul mediu per zi')
axes[1, 1].set_xlabel('Ziua saptamanii')
axes[1, 1].set_ylabel('Bacsis mediu ($)')

plt.tight_layout()
plt.savefig('dashboard_tips.png', dpi=150, bbox_inches='tight')
plt.show()