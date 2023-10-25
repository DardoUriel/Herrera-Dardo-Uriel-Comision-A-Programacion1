"""16.	Solicitar al usuario un número entero y luego un dígito. 
Informar la cantidad de ocurrencias del dígito en el número, utilizando para ello una función que calcule la frecuencia."""
from functions import count_digit_occurrences
# Solicita al usuario un número entero.
number = input("Ingrese un número entero: ")
# Solicita al usuario un dígito.
digit = input("Ingrese un digito: ")

if len(digit) != 1 or not digit.isdigit():
    print("Tiene que ingresar un solo digito")
elif not number.isdigit():
    print("El número no tiene enteros o tiene un signo que no es entero")
else:
    occurrences = count_digit_occurrences(number, digit)
    print(f"El digito {digit} aparece {occurrences} veces en el número {number}.")
