"""6-	Hacer un programa que permita saber si un año es bisiesto. 
Para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100, excepto que también sea divisible por 400."""
year = int(input("Escriba un año para saber si es bisiesto: "))
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0): #calculo que sea divisible por 4, que no sea divisible por 100 a menos que sea por 400
    print(f"El año {year} es bisiesto!!!")
else:
    print(f"El año {year} no es bisiesto!!!")