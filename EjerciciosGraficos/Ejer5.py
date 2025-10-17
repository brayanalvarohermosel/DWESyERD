import matplotlib.pyplot as plt

# ● Futbol: nois = 12, noies = 6
# ● Bàsquet: nois = 10, noies = 8
# ● Volei: nois = 5, noies = 12
# ● Representa-ho en un gràfic de barres apilades (nois i noies).

male = [12,10,5]
female = [6,8,12]
sport = ["futbol", "basquet", "Voley"]

plt.figure(figsize=(7,5))
plt.bar(sport, male, color = "blue", label = "Male")
plt.bar(sport, female,bottom = male, color = "pink", label = "Female")
plt.ylabel("Participantes")
plt.legend()
plt.show()