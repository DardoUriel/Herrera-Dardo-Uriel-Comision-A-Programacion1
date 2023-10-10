"""2.	Dados los catetos de un triángulo rectángulo, calcular su hipotenusa."""
leg1 = float(input("Escriba el largo del cateto 1: "))
leg2 = float(input("Escriba el largo del cateto 2: "))
hypotenuse = (leg1**2 + leg2**2) ** (1/2) #calculo la hipotenusa
print(f"La hipotenusa es: {hypotenuse}")
