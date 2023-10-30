"""14.	Requerir al usuario que ingrese un número entero e informar si es primo o no, utilizando una función booleana que lo decida."""
import sys
sys.path.append("C:/Users/FlowUser/Desktop/UTN/ProgrmacionRepositorio/Herrera-Dardo-Uriel-Comision-A-Programacion1/Funciones")
from functions import prime_detecter

number = int(input("Ingrese un número entero: "))

if prime_detecter(number):
    print(f"{number} es primo")
else:
    print(f"{number} no es primo")
