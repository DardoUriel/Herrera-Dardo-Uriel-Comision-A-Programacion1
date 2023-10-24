#22-	Solicitar al usuario que ingrese números enteros positivos y, por cada uno, 
#imprimir la suma de los dígitos que lo componen. La condición de corte es que se ingrese el número -1. 
#Al finalizar, mostrar cuántos de los números ingresados por el usuario fueron números pares.
suma=0
aux=0
cont=0
while True:
    number = int(input("ingrese un numero: "))
    if number%2==0:
        cont+=1
    if number>0:
        if number>9:
            while True:
                aux=number%10
                number=number//10
                suma+=aux
                if number<10:
                    print(f"la suma de los digitos {suma+number}")
                    break
        else:
            print(number)
    elif number==-1:
        break
print(f"hay {cont} numeros pares")