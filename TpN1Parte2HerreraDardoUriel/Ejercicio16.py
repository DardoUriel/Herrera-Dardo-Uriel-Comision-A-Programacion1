"""16.	Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales."""
name = input("Escriba su nombre: ")
surname = input("Escriba su apellido: ")
surname2 = input("Escriba su segundo apellido: ")
print(f"Sus iniciales son: {name[0].upper()}. {surname[0].upper()}. {surname2[0].upper()}.") #los strings son tratados como arrays de caracteres donde se les saca la primer posición y se pone en mayusculas