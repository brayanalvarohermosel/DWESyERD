import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

csv_path = Path(__file__).parent / "ventas_mensuales.csv"
if not csv_path.exists():
    csv_path = Path("JOURNAL") / "EjerciciosGraficos" / "ventas_mensuales.csv"

df = pd.read_csv(csv_path)

df = df.rename(columns=lambda s: s.strip())
if 'Mes' not in df.columns or 'Ventas' not in df.columns:
    raise SystemExit("El CSV ha de contenir les columnes 'Mes' i 'Ventas'")

df['Ventas'] = pd.to_numeric(df['Ventas'], errors='coerce')
df = df.dropna(subset=['Ventas']).reset_index(drop=True)

mes_numeric = pd.to_numeric(df['Mes'], errors='coerce')
if mes_numeric.notna().all():
    df = df.assign(Mes_ord=mes_numeric).sort_values('Mes_ord')

# Gràfic de barres
plt.figure(figsize=(15, 5))
plt.bar(df['Mes'], df['Ventas'], color='C0')
plt.title('Ventas mensuals - Barras')
plt.xlabel('Mes')
plt.ylabel('Ventas (€)')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# Grafico de línia con la evolución
plt.figure(figsize=(12, 5))
plt.plot(df['Mes'], df['Ventas'], marker='o', linestyle='-')
plt.title('Evolución de ventas - Linea')
plt.xlabel('Mes')
plt.ylabel('Ventas (€)')
plt.grid(True)
plt.tight_layout()
plt.show()

# Histograma de la distribucion
plt.figure(figsize=(6, 4))
plt.hist(df['Ventas'], bins=8, color='C2', edgecolor='k', alpha=0.75)
plt.title('Distribución de las ventas')
plt.xlabel('Ventas (€)')
plt.ylabel('Frecuencia')
plt.tight_layout()
plt.show()