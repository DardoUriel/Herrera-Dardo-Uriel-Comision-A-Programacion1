"""17.	Solicitar al usuario el ingreso de números primos. 
La lectura finalizará cuando ingrese un número que no sea primo. Por cada número, mostrar la suma de sus dígitos. 
También solicitar al usuario un dígito e informar la cantidad de veces que aparece en el número (frecuencia). 
Al finalizar el programa, mostrar el factorial del mayor número ingresado."""
import sys
sys.path.append("C:/Users/FlowUser/Desktop/UTN/ProgrmacionRepositorio/Herrera-Dardo-Uriel-Comision-A-Programacion1/Funciones")
from functions import *
import math
nums = []
while True:
    number = input("Ingrese un número entero primo (termina si ingresa un número no primo): ")
    if not number.isdigit():
        print("El número no tiene enteros o tiene un signo que no es entero")
    else:
        number = int(number)
        if prime_detecter(number):
            print(f"El número {number} es primo")
            nums.append(number)
        else:
            print(f"El número {number} no es primo\n")
            break

for i in range(len(nums)):
    print(f"El número {i+1} es: {nums[i]}")
    print(f"La suma de sus dígitos es: {sumar_digitos(nums[i])}")
    while True:
        digit = input(f"Qué digito quiere contar del número {nums[i]}?\n")
        if not digit.isdigit():
            print("Tiene que ingresar un solo digito")
        else:
            num_temp = str(nums[i])
            print(f"La cantidad de veces que aparece el dígito {digit} es: {count_digit_occurrences(num_temp, digit)}\n")
            break
if nums :
    num_max = max(nums)
    print(f"\nEl factorial del número mayor {num_max} es: {math.factorial(num_max)}\n")
else:
    print("\nNO se han ingresado número primos!!!")