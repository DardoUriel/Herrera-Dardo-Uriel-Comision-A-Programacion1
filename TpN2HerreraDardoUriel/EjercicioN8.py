"""8-	Escribí un programa que solicite ingresar un nombre de usuario y una contraseña. 
Si el nombre es “Gwenevere” y la contraseña es “excalibur”, mostrar en pantalla “Usuario y contraseña correctos. 
Puede ingresar a Camelot”. Si el nombre o la contraseña no coinciden, mostrar “Acceso denegado”."""
user_name = input("Ingrese el nombre de usuario: ")
password = input("Ingrese la contraseña: ")
if user_name == "Gwenevere" and password == "excalibur":
    print("Usuario y contraseña correctos. Puede ingresar a Camelot!!")
else:
    print("Acceso denegado")