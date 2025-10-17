import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 300)
y1 = np.sin(x)
y2 = np.cos(2 * x)

fig, ax = plt.subplots(figsize=(8, 5))
fig.suptitle("Grafico de funciones trigonometricas", fontsize=16, fontweight="bold")
ax.set_title("Seno y coseno con colores, grosores y tipos de puntos", fontsize=10)

ax.plot(x, y1, color="#1f77b4", linewidth=2.5, marker="o", markevery=25, markersize=6, label="sin(x)")
ax.plot(x, y2, color="#ff7f0e", linewidth=1.8, linestyle="--", marker="s", markevery=30, markersize=6, label="cos(2x)")

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.grid(alpha=0.3)
ax.legend(title="Legenda")

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig("graf.png", dpi=300, bbox_inches="tight")
plt.show()