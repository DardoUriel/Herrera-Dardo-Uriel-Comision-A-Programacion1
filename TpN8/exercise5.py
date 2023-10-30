#Escribir una función recursiva que encuentre el mayor elemento de una lista.
import sys
sys.path.append("C:/Users/FlowUser/Desktop/UTN/ProgrmacionRepositorio/Herrera-Dardo-Uriel-Comision-A-Programacion1/Funciones")
from functions import encontrar_mayor


mi_lista = [5, 16, 2, 57, 10, 60, 70, 80, 90, 100]
mayor = encontrar_mayor(mi_lista)
print("El mayor elemento de la lista es:", mayor)