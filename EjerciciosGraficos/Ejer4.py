import matplotlib.pyplot as plt

# ● Vendes de dos productes (A i B) durant 6 mesos.
# ● Fes un gràfic de línia amb dues sèries i llegenda.

months = ["Jenuary", "February", "March", "April", "May", "Juni"]
productA = [4,2,5,7,6,9]
productB = [8,9,4,6,3,7]


plt.figure(figsize = (15,6))
plt.plot(months, productA, marker = 0, color = "blue", label = "Producto A")
plt.plot(months, productB, marker = 0, color = "red", label = "Producto B")
plt.title("Temperature Average")
plt.xlabel("Meses")
plt.ylabel("Ventas")
plt.legend()
plt.show()