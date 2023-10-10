"""13.	Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número invertido. Ejemplo, si se introduce 23 que muestre 32."""
num = int(input("Ingrese un número de dos cifras: "))
if 10 <= num <= 99: #comprueba que sea de 2 cifras
    
    units = num % 10 #calcula unidades
    tens = num // 10 #calcula decenas

    print(f"El número de dos cifras invertido es: {(units * 10) + tens}") #unidades * 10 se vuelven decenas, y las decenas ya estaban guardadas como unidades
else:
    print("El número ingresado no es de dos cifras.")