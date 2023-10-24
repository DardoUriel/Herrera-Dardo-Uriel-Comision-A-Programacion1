#5.	Escribe un programa que imprima todos los números pares del 1 al 20 usando un bucle for.
#Utiliza la declaración continue para omitir los números impares.
for i in range(1,20+1,1):
    if i%2==0:
        print(f"{i} es un numero par")#es par
    else:
        print(f"{i} no es un numero par")#es impar
        continue
