"""2-	Hacer que el programa anterior muestre un mensaje de error si el usuario digita un número negativo."""
how_old=  int(input("Ingresar cuantos años tiene la computadora: "))
if how_old < 0: #se comprueba si es positivo
    print("La cantidad de años no puede ser negativa!!!")
elif how_old <=2:
    print("Es una computadora nueva!!!")
else:
    print("Es una computadora vieja!!!")