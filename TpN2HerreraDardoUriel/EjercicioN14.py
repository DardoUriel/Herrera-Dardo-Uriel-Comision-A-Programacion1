"""14-	Escriba un programa que pida los coeficientes de una ecuación de primer grado (a x + b = 0) y escriba la solución.
Se recuerda que una ecuación de primer grado puede no tener solución, tener una solución única, o que todos los números sean solución. Se recuerda que la fórmula de las soluciones es 
x = -b / a"""
a = float(input("Ingrese el coeficiente a: "))
b = float(input("Ingrese el coeficiente b: "))
if a == 0:
    if b == 0:
        solucion = "La ecuación tiene infinitas soluciones!!"# Calcular la solución de la ecuación
    else:
        solucion = "La ecuación no tiene solución!!"
else:
    solucion = f"La solución de la ecuación es x = {round(-b / a,2)}"
print(solucion)