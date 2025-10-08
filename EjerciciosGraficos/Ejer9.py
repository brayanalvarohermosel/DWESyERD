import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = {
    'Matemàtiques': [7, 8, 6, 9, 5, 8, 7, 6, 9, 10, 5, 7],
    'Història': [6, 7, 8, 7, 6, 7, 8, 7, 6, 7, 8, 7],
    'Anglès': [5, 6, 7, 8, 9, 6, 5, 7, 8, 6, 5, 7]
}

df = pd.DataFrame(data)
df_melted = df.melt(var_name='Asignatura', value_name='Nota')

plt.figure(figsize=(8, 6))
sns.boxplot(x='Asignatura', y='Nota', data=df_melted)
plt.title('Variabilidad de las notas por asignatura')
plt.show()