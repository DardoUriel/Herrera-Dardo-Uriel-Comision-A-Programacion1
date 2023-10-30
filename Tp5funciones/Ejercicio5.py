'''5.	Crear una función que calcule la temperatura media de un día a partir de la temperatura máxima y mínima.
Crear un programa principal, que utilizando la función anterior,
vaya pidiendo la temperatura máxima y mínima de cada día y vaya mostrando la media. 
El programa pedirá el número de días que se van a introducir.'''
import sys
sys.path.append("C:/Users/FlowUser/Desktop/UTN/ProgrmacionRepositorio/Herrera-Dardo-Uriel-Comision-A-Programacion1/Funciones")
from functions import half
amout = int(input("ingrese la cantidad de dias que quiere: "))
for i  in range(amout):
    print(f"dia {i+1}")
    max = int(input("ingrese la temperatura maxima: "))
    min = int(input("ingrese la temperatura minima: "))
    print(half(max,min))
    
    