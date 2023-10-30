"""11.	Escribir una función que reciba otra función y una lista, 
y devuelva otra lista con el resultado de aplicar la función dada a cada uno de los elementos de la lista."""
import sys
sys.path.append("C:/Users/FlowUser/Desktop/UTN/ProgrmacionRepositorio/Herrera-Dardo-Uriel-Comision-A-Programacion1/Funciones")
from functions import func_applier
num_coleccions = []
while True:
    num = int(input("Escriba números enteros (Cuando quiera parar, escriba 0): "))
    if num == 0: #condicional de salida
        break
    else:
        num_coleccions.append(num)
num_coleccions = func_applier(num_coleccions) #actualiza la lista
print("Los números siguientes a los números ingresados son: \n")
for i in num_coleccions:
    print(i, end=" ") #imprime la nueva lista
print("\n")