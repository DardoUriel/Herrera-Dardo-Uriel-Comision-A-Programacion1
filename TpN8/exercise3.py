#Escribir una funcion recursiva que reciba como parámetros dos strings a y b,
# y devuelva una lista con las posiciones en donde se encuentra b dentro de a.
import sys
sys.path.append("C:/Users/FlowUser/Desktop/UTN/ProgrmacionRepositorio/Herrera-Dardo-Uriel-Comision-A-Programacion1/Funciones")
from functions import word_in_sentence
a = "Un tete a tete Cib Tete"
b = "te"

positions = word_in_sentence(a, b,0,None)
print(f"Posiciones en las que se encuentra {b} en {a}:",positions)