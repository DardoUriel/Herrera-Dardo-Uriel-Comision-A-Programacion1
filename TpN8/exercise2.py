

#Escribir una función que reciba 2 enteros n y b y devuelva True si n es potencia de b.

import sys
sys.path.append("C:/Users/FlowUser/Desktop/UTN/ProgrmacionRepositorio/Herrera-Dardo-Uriel-Comision-A-Programacion1/Funciones")
from functions import potency
n = int(input("Ingrese un numero: "))
b = int(input("Ingrese un numero: "))

resultado = potency(b, n)
if resultado:
    print(f"{n} es una potencia de {b}")
else:
    print(f"{n} no es una potencia de {b}")


