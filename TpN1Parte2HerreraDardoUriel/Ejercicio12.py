"""12.	Realizar un algoritmo que lea un número y que muestre su raíz cuadrada y su raíz cúbica."""
num = float(input("Escriba un número: "))
print(f"La raíz cuadrada de {num} es: {round(num ** (1/2), 3)}")
print(f"La raíz cúbica de {num} es: {round(num ** (1/3), 3)}")