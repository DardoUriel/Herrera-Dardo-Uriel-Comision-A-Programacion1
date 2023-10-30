"""15.	Escribir un programa que pida números al usuario, motrar el factorial de cada uno y, al finalizar, 
la cantidad total de números leídos en total. Utilizar una o más funciones, según sea necesario."""
import sys
sys.path.append("C:/Users/FlowUser/Desktop/UTN/ProgrmacionRepositorio/Herrera-Dardo-Uriel-Comision-A-Programacion1/Funciones")
from functions import factorials
nums = []
cuantity = 0
while True:
    nums.append(int(input("Ingrese un número entero: ")))
    cuantity +=1
    fin = input("Quiere salir? (1) para si: ")
    if fin == "1":
        break
factorials = factorials(nums)
for i in range(len(nums)):
    print(f"El factorial de {nums[i]} es {factorials[i]}")
print(f"Total de números: {cuantity}")