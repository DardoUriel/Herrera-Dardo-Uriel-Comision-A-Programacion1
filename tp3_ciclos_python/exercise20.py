#20-	Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, 
#mostrar la sumatoria de todos los números ingresados.
addition=0
while True:
    number = int(input("ingrese un numero: "))
    if number==0:
        break
    addition+=number
print(addition)