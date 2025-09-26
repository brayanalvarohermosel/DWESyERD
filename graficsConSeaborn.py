import seaborn as sns
import matplotlib.pyplot as plt

# Exemple amb dades simples
notes = [5, 6, 7, 8, 5, 9, 6, 7, 8, 10]

sns.histplot(notes, bins=5, kde=True)
plt.title("Distribució de notes")
plt.show()