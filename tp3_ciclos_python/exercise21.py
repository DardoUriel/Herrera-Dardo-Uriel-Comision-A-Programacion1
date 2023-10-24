#21-	Leer números enteros positivos de teclado, 
#hasta que el usuario ingrese el 0. Informar cuál fue el mayor número ingresado.

bigger_number=0
while True:
    number = int(input("ingrese un numero: "))
    if number==0:
        break
    elif number>bigger_number:
        bigger_number=number
print(f"el numeor mayor es {bigger_number}")