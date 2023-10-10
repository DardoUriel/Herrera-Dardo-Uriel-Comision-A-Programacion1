"""6.	Calcular la media de tres números pedidos por teclado."""
print("Escriba 3 números a promediar")
num1 = float(input("Número a promediar N1: "))
num2 = float(input("Número a promediar N2: "))
num3 = float(input("Número a promediar N3: "))
print(f"El promedio es: {round((num1 + num2 + num3) / 3, 2)}")