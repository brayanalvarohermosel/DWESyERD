import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

platforms = ['WhatsApp', 'Instagram', 'TikTok', 'Twitter', 'Facebook']
alpha = np.array([6.0, 5.0, 6.5, 2.5, 3.5])
shares = np.random.default_rng().dirichlet(alpha) * 100
order = np.argsort(-shares)
platforms = [platforms[i] for i in order]
shares = shares[order]

colors = plt.get_cmap('tab10').colors[:len(platforms)]

fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(12, 6))

explode = [0.08 if i == 0 else 0 for i in range(len(shares))]
ax1.pie(shares, labels=platforms, autopct='%1.1f%%', startangle=140,
    colors=colors, explode=explode, shadow=True, textprops={'fontsize': 10})
ax1.set_title("Distribución de uso por red social")

bars = ax2.bar(platforms, shares, color=colors)
ax2.set_ylabel('Porcentage de uso (%)')
ax2.set_ylim(0, max(shares) * 1.2)
ax2.set_title('Comparación: grafico de barras')

for bar, val in zip(bars, shares):
    ax2.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.8,
         f'{val:.1f}%', ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.show()