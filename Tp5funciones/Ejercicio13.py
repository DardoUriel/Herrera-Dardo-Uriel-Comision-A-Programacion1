"""13.	Escribir una función que calcule el módulo de un vector."""
import sys
sys.path.append("C:/Users/FlowUser/Desktop/UTN/ProgrmacionRepositorio/Herrera-Dardo-Uriel-Comision-A-Programacion1/Funciones")
from functions import modulus_of_a_vector
vectors = []
for i in range(1,4):
    vectors.append(float(input(f"Escriba el valor del vector n{i}: ")))
modulus = modulus_of_a_vector(vectors) #se llama a la funcion del vector

print(f"El módulo del vector es: {round(modulus, 3)}")
