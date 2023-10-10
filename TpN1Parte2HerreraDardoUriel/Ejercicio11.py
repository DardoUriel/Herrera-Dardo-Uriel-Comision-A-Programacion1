"""11.	Pide al usuario dos números y muestra la “distancia” entre ellos (el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo)."""
num1 = float(input("Escriba el primer número: "))
num2 = float(input("Escriba el segundo número: "))
print(f"La distancia entre {num1} y {num2} es de: {num1 - num2}") if num1 > num2 else print(f"La distancia entre {num1} y {num2} es de: {num2 - num1}") #hace que al mayor se le reste el menor, asi siempre queda positivo, incluso si son números negativos