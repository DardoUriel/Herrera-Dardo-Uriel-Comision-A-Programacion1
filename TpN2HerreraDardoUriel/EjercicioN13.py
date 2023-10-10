"""13-	Escriba un programa que pida dos números enteros y que escriba si el mayor es múltiplo del menor. 
Haciendo que el programa avise cuando se escriben valores negativos o nulos."""
num1 = int(input("Escribe el primer número (entero y mayor a 0): "))
num2 = int(input("Escribe el segundo número (entero y mayor a 0): "))
if num1 > num2:
    bigger = num1
    lower = num2
else:
    bigger = num2
    lower = num1

if num1 < 1 or num2 < 1:
    print("Alguno de los números no son mayores a 0")
elif bigger % lower == 0:
    print(f"{bigger} es multiplo de {lower}")
else:
    print(f"{bigger} no es multiplo de {lower}")