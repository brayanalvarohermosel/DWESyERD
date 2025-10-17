import numpy as np
import matplotlib.pyplot as plt

months = np.array(['Gen', 'Feb', 'Mar', 'Abr', 'Mai', 'Jun'])
sales = np.array([120, 150, 90, 200, 170, 130])
ads = np.array([20, 30, 15, 40, 35, 25])
product_categories = ['Producto A', 'Producto B', 'Producto C', 'Producto D']
product_sales = np.array([450, 300, 150, 100])

fig, axs = plt.subplots(2, 2, figsize=(10, 8))
fig.suptitle('Dashboard sencillo: ventas — 4 graficos', fontsize=14)

ax = axs[0, 0]
bars = ax.bar(months, sales, color='tab:blue')
ax.set_title('Ventas por mes (barras)')
ax.set_ylabel('Unidades vendidas')
ax.grid(axis='y', linestyle='--', alpha=0.4)

for b in bars:
    h = b.get_height()
    ax.text(b.get_x() + b.get_width()/2, h + 3, str(h), ha='center', va='bottom', fontsize=8)

ax = axs[0, 1]
ax.pie(sales, labels=months, autopct='%1.1f%%', startangle=90, colors=plt.cm.Pastel1.colors)
ax.set_title('Distribución porcentual de ventas (pie)')
ax.axis('equal')

ax = axs[1, 0]
ax.hist(sales, bins=5, color='tab:green', edgecolor='black', alpha=0.7)
ax.set_title('Histograma de ventas')
ax.set_xlabel('Unidades vendidas')
ax.set_ylabel('Frecuencia')
ax.grid(axis='y', linestyle='--', alpha=0.4)

ax = axs[1, 1]
ax.scatter(ads, sales, color='tab:red', s=60)
slope, intercept = np.polyfit(ads, sales, 1)
x_line = np.linspace(ads.min()-5, ads.max()+5, 100)
y_line = slope * x_line + intercept
r_value = np.corrcoef(ads, sales)[0, 1]
ax.plot(x_line, y_line, color='gray', linestyle='--', label=f"r={r_value:.2f}")
ax.set_title('Publicidad vs Ventas (scatter + regresión)')
ax.set_xlabel('Despensa publicitaria')
ax.set_ylabel('Unidades vendidas')
ax.legend()

plt.tight_layout(rect=[0, 0.03, 1, 0.95])

plt.show()
