"""3-	Solicitar al usuario que ingrese los nombres de dos personas, los cuales se almacenarán en dos variables. 
A continuación. Imprimir ‘coincidencia’ si ambos nombres comienzan con la misma letra. Si no es así, imprimir ‘no hay coincidencia’."""
name1 = input("Escriba el nombre de la primer persona: ")
name2 = input("Escriba el nombre de la segunda persona: ")
print("Hay coincidencia en la primer letra!!!") if name1[0].upper() == name2[0].upper() else print("No hay coincidencia en la primer letra...") #se comparan las primeras letras en mayusculas