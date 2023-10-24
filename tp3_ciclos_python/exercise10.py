#10-	Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
'''Escribir un programa que pida al usuario un número entero
y muestre por pantalla si es un número primo o no.'''
number = int(input("ingresar un numero entero"))
divisors = 0
for i in range (number,0,-1):
    if number%i == 0:
        divisors += 1
if divisors == 2:
    print("el numero es primo")
else:
    print("el numero NO es primo")