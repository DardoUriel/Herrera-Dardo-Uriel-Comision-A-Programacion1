"""1-	Crear un programa que reciba el número de años que tiene nuestra computadora y muestre en la consola que el computador es nuevo si es menor o igual a 2 años
y que el computador es viejo si es mayor a 2 años."""
how_old=  int(input("Ingresar cuantos años tiene la computadora: "))
print("Es una computadora nueva!!!") if how_old <=2 else print("Es una computadora vieja!!!")