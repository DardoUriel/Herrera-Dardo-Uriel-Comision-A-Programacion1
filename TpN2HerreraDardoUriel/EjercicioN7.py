"""7-	Escribí un programa para solicitar al usuario tres números y mostrar en pantalla al menor de los tres."""
num1 = int(input("Escribe el primer número: "))
num2 = int(input("Escribe el segundo número: "))
num3 = int(input("Escribe el tercer número: "))
if num1 == num2 and num2 == num3: #se comprueba primero si son iguales
    print("Los 3 números son iguales!!")
else:
    minimum = min(num1, num2, num3) #funcion min para saber cual es el menor entre diferentes variables
    print(f"El número menor es: {minimum}")
