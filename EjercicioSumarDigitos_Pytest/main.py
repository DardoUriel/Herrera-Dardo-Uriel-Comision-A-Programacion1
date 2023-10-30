import sys
sys.path.append("C:/Users/FlowUser/Desktop/UTN/ProgrmacionRepositorio/Herrera-Dardo-Uriel-Comision-A-Programacion1/Funciones")
from functions import sumar_digitos
while True:
    number = int(input("ingrese un numero: "))
    if number !=0:
        print(sumar_digitos(number))
    else:
        break