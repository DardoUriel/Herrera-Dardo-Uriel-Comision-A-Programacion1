#Escribir dos funciones mutualmente recursivas par(n) e impar(n) que determinen la paridad del numero natural dado, conociendo solo que:
# 1 es impar.
#Si un número es impar, su antecesor es par; y viceversa.
import sys
import sys
sys.path.append("C:/Users/FlowUser/Desktop/UTN/ProgrmacionRepositorio/Herrera-Dardo-Uriel-Comision-A-Programacion1/Funciones")
from functions import odd,even

n = int(input("Ingrese n: "))
even(n)       