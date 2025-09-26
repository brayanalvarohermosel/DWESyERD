import matplotlib.pyplot as plt

fruites = ["Pomes", "Peres", "Plàtans", "Taronges"]
quantitats = [50, 30, 70, 45]

plt.bar(fruites, quantitats, color="green")
plt.title("Consum de fruita")
plt.xlabel("Tipus de fruita")
plt.ylabel("Quantitat")
plt.show()