"""15-	Escriba un programa que pregunte primero si se quiere calcular el área de un triángulo o la de un círculo. 
Si se contesta que se quiere calcular el área de un triángulo (escribiendo T o t), el programa tiene que pedir entonces la base y la altura y escribir el área. 
Si se contesta que se quiere calcular el área de un círculo (escribiendo C o c), el programa tiene que pedir entonces el radio y escribir el área."""
import math
opcion = input("¿Quiere calcular el área de un triángulo (T) o un círculo (C)? ").upper()
if opcion == "T":
    base = float(input("Ingrese la base del triángulo: "))# Calcular el área de un triángulo
    higth = float(input("Ingrese la altura del triángulo: "))
    area = 0.5 * base * higth
    print(f"El área del triángulo es: {round(area,2)}")
elif opcion == "C":
    radio = float(input("Ingrese el radio del círculo: "))# Calcular el área de un círculo
    area = math.pi * radio**2
    print(f"El área del círculo es: {round(area,2)}")
else:
    print("Opción no válida!!")
