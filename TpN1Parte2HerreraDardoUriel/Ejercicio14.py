"""14.	Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar un algoritmo que intercambie los valores de ambas variables y muestre cuanto valen al final las dos variables."""
A = input("Escriba el valor de la variable A: ")
B = input("Escriba el valor de la variable B: ")
aux = A
A = B
B = aux #se intercambian las variables con ayuda de un auxiliar
print(f"Nuevo valor de las variables A: '{A}' y B: '{B}'")