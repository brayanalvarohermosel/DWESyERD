import matplotlib.pyplot as plt
import numpy as np

# ● Percentatges d’ús de navegadors: Chrome 65%, Firefox 20%, Safari 10%,
# Altres 5%.
# ● Representa-ho amb un gràfic circular i mostra el percentatge a cada porció.


fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

navegador = ["Chrome 65",
          "Firefox 20",
          "Safari 10",
          "Otros 5"]

data = [float(x.split()[1]) for x in navegador]
ingredients = [x.split()[-1] for x in navegador]


def func(pct, allvals):
    absolute = int(np.round(pct/100.*np.sum(allvals)))
    return f"{pct:.1f}%\n"


wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                  textprops=dict(color="w"))

plt.setp(autotexts, size=8, weight="bold")

ax.set_title("Porcentage de uso del navegador:")

plt.show()