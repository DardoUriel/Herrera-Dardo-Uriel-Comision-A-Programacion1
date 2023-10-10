"""4.	Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius."""
fahrenheit = float(input("Escriba la cantidad de grados Fahrenheit: "))
celsius = (fahrenheit - 32)*5/9 #formula para convertir
print(f"{fahrenheit} grados Fahrenheit se traslada a {round(celsius, 2)} grados Celsius")