import seaborn as sns
import matplotlib.pyplot as plt
import random

# Genera una llista de 50 notes aleatòries entre 4 i 10
# Crea el gràfic amb histograma i corba de densitat
notes = [random.uniform(4, 10) for _ in range(50)]

sns.histplot(notes, kde=True, bins=10, color='skyblue', edgecolor='black')

plt.xlabel('Nota')
plt.ylabel('Frecuencia')
plt.title('Histograma de notas con curva de densidad')
plt.show()