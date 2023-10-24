'''2.	Escriba un programa que administre una cuenta bancaria, usando una bitácora de operaciones.
La bitácora de operaciones tiene la siguiente forma:
D 100
R 50

D 100 significa que depositó 100 pesos
R 50 significa que retiró 50 pesos

Ejemplo de una entrada:
D 200
D 200
R 100
D 50
Introducir una línea vacía indica que ha finalizado la bitácora.
La salida de éste programa sería:
350
'''
while True:
    option = input("ingrese (d) si desea depositar , ingrese (r) para retirar: ")#opciones
    if option.lower() =="d":
        d = int(input("ingrese una cantidad a depositar: "))#depositar
    elif option.lower() =="r":
        r = int(input("ingrese una cantidad a retirar: "))#retirar
    elif option=="":
        break
    else:
        continue
print(f"el total es de {d-r}")#cuenta de datos ingresados

