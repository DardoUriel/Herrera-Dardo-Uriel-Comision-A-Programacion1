'''
3.	Escribir un programa que permita al usuario obtener un identificador para cada uno de los socios de un club.
Para eso ingresará nombre completo y número de DNI de cada socio, indicando que finalizará el procesamiento mediante el ingreso de un nombre vacio.
Precondición: el formato del nombre de los socios será: nombre apellido. Podría ingresarse más de un nombre, en cuyo caso será: nombre1, nombre2, apellido.
Si un socio tuviera más de un apellido, el usuario solo ingresará uno.
Se debe validar que el número de DNI tenga 7 u 8 dígitos. En caso contrario, el programa debe dejar al usuario en un bucle hasta que ingrese un DNI correcto.
Por cada socio se debe imprimir su identificador único, el cual estará formado por: el primer nombre, la cantidad de letras del apellido y
los 3 primeros dígitos de su DNI. Ejemplo:
Nombre: María Ines Rosales
DNI: 25469648
ID -> Maria7254
'''
from ..functions import *
while True: #valida el formato del nombre
    name  = input("nombre/s y apellido: ")
    if validate_format_full_name(name) == True:
        break
    else:
        print("el fomato no es  el correcto , el formato es (nombre nombre apellido/nombre apellido)")

while True:
    dni = input("DNI: ")
    if(number_dni_validate(dni) == False ):#valida dni
        print("dni invalido, debe tener entre 7 y 8 digitos")
    else:
        break
print(create_identifier(name,dni))#devulve identificador