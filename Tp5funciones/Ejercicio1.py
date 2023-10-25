'''1.Escribir una función que, dado un número de DNI, retorne True si el número es válido y False si no lo es.
Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos.
'''

from ..functions import number_dni_validate
number = input("ingresar dni sin espacios: ")
print(number_dni_validate(number))#imprime true si la longitud de l dni esta entre 7 y 8, sino imprime false