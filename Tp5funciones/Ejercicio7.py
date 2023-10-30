'''
Crea una función que recibe una lista con valores numéricos y 
devuelve el valor máximo y el mínimo.
Crea un programa que pida números por teclado
y muestre el máximo y el mínimo, utilizando la función anterior.
'''
import sys
sys.path.append("C:/Users/FlowUser/Desktop/UTN/ProgrmacionRepositorio/Herrera-Dardo-Uriel-Comision-A-Programacion1/Funciones")
from functions import max_and_min_value
numbers = [1,12,45,10,3,4,9,6]
print(max_and_min_value(numbers))