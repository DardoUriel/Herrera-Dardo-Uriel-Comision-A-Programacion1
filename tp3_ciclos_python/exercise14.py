#14-	Escriba un programa que pida dos números enteros y 
#escriba qué números son pares y cuáles impares desde el primero hasta el segundo.
cont=0
while cont<2:
    number1 = int(input("ingrese un numero: "))
    cont+=1
    if number1%2==0:
        print(f"el numero {number1} es par")
    else:
        print(f"el numero {number1} es impar")
