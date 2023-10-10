"""16-	Haz una calculadora básica pida al usuario dos valores, a y b.
Según la opción que desean, realizar la operación:
•	Si operación es 1 entonces debemos ver el resultado de a + b
•	Si operación es 2 entonces debemos ver el resultado de a * b
•	Si operación es 3 entonces debemos ver el resultado de a - b
•	Si operación es 4 entonces debemos ver el resultado de a / b"""
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
operacion = int(input("Elija la operación que desea realizar:\n" "1. Suma\n" "2. Multiplicación\n" "3. Resta\n" "4. División\n" "Ingrese el número de la operación: ")) #Se muestran las opciones con saltos de linea
if operacion == 1: #Se calculan depende la opcion
    result = a + b
    print(f"El resultado de la suma es: {result}")
elif operacion == 2:
    result = a * b
    print(f"El resultado de la multiplicación es: {result}")
elif operacion == 3:
    result = a - b
    print(f"El resultado de la resta es: {result}")
elif operacion == 4:
    if b != 0:
        result = a / b
        print(f"El resultado de la división es: {round(result,3)}")
    else:
        print("No es posible dividir por cero!!")
else:
    print("Operación no válida!!")