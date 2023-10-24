'''3.	Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, 
finalizando cuando se reciba un cero.
Imprimir la cantidad total de números primos ingresados.
Nota: Un número primo es un número natural mayor que 1 que tiene únicamente dos divisores distintos: 
él mismo y el 1.
'''
cont=0
while True:
    number=int(input("ingrese un numero mayor a uno: "))
    if number>=1:
        for i in range(number,0,-1):
            if number%i==0:
                cont+=1
        if cont==2:
            print(f"{number} es un numero primo")
        else:
            print(f"{number} no es un numero primo")
    elif number==0:
        break
    else:
        continue
