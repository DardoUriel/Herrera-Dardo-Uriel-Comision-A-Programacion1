#1.	Escribir una función que reciba un número positivo n y devuelva la cantidad de dígitos que tiene.


import sys
sys.path.append("C:/Users/FlowUser/Desktop/UTN/ProgrmacionRepositorio/Herrera-Dardo-Uriel-Comision-A-Programacion1/Funciones")
from functions import number_of_digits

num = int(input("ingrese un numero: "))
cont = 0
print(number_of_digits(num , cont))
