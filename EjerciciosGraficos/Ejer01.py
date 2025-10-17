import matplotlib.pyplot as plt

# Llista amb les temperatures mitjanes de cada mes d’un any.
# Fes un gràfic de línia amb punts.
# Afegeix títol i etiquetes als eixos.

months = ["Jenuary", "February", "March", "April", "May", "Juni", "July", "August", "September", "October", "November", "December"]
temperature = [15,45,30,48,35,79,34,48,29,34,28,46]

plt.figure(figsize = (15,5))
plt.plot(months, temperature, marker = 0, color = "blue")
plt.title("Temperature Average")
plt.xlabel("Months")
plt.ylabel("Temperature")
plt.show()
