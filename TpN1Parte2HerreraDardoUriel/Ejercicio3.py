"""3.	Dados dos números, mostrar la suma, resta, división y multiplicación de ambos."""
num1 = float(input("Escriba el primer número: "))
num2 = float(input("Escriba el segundo número: "))
print(f"El resultado de la suma entre los dos números es: {num1 + num2}")
print(f"El resultado de la resta entre {num1} y {num2} es: {num1 - num2}")
print(f"El resultado de la resta entre {num2} y {num1} es: {num2 - num1}")
print(f"El resultado de {num1} dividido {num2} es: {num1/num2}") if num2 != 0 else print(f"El resultado de {num1} dividido {num2} no se puede mostrar ya que no se puede dividir por 0")
print(f"El resultado de {num2} dividido {num1} es: {num2/num1}") if num1 != 0 else print(f"El resultado de {num2} dividido {num1} no se puede mostrar ya que no se puede dividir por 0")
print(f"El resultado de la multiplicación entre los dos números es: {num1 * num2}")