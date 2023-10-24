
'''4.	Escribir un programa que permita al usuario ingresar dos años y 
luego imprima todos los años en ese rango, que sean bisiestos y múltiplos de 10.
Nota: Para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100, 
excepto que también sea divisible por 400.
'''
year = int(input("ingrese un año: "))
year2 = int(input("ingrese un año: "))
for i in range(year,year2,1):
    if i%4==0 and i%100!=0 or i%400==0:
        print(f"{i} es un año bisiesto")
    else:
        print(f"{i} no es un año bisiesto")
