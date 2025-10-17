import matplotlib.pyplot as plt

# Dona una llista amb fruites i una llista amb el nombre de persones que les han triat.
# Representa-ho amb un gràfic de barres.
# Pinta cada barra d’un color diferent.

fruits = ["Apple", "Orange", "Lemon", "Watermelon", "Coconut"]
people = [7,8,6,4,8]

plt.bar(fruits, people, color="green")
