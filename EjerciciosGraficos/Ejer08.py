import matplotlib.pyplot as plt

studyTime = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
notes = [4, 5, 5.5, 6, 6.5, 7, 7.5, 8, 9, 9.5]

plt.scatter(studyTime, notes, color='blue')
plt.xlabel('Horas de estudio')
plt.ylabel('Notas obtenidas')
plt.title('Relación entre horas de estudio y notas')
plt.grid(True)
plt.show()
