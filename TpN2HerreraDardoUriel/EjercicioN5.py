"""5-	Escribir un programa que solicite al usuario una letra, si es una vocal, mostrar el mensaje ‘Es vocal’.
Se debe validar que el usuario ingrese sólo un carácter. Si ingresa un string de más de un carácter, informarle que no se puede procesar el dato.
"""
letter = input("Escriba una letra: ")
if len(letter) > 1: #se ve si tiene más de un caracter
    print("Tiene que ser solo una letra, no se puede procesar el dato!!")
elif letter.upper() == "A" or letter.upper() == "E" or letter.upper() == "I" or letter.upper() == "O" or letter.upper() == "U":
    print("La letra es una vocal!!")
else:
    print("La letra no es una vocal!!")