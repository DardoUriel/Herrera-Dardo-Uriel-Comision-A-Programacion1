"""9-	Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
El grupo A está formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. 
Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde."""
name = input("Ingrese su nombre: ")
gender = input("Ingrese su sexo (F o M): ")
# Convertir el nombre a mayúsculas
name = name.upper()

# Verificar el grupo al que pertenece el alumno
if (gender == "F" and name[0] < "M") or (gender == "M" and name[0] > "N"):
    group = "A"
else:
    group = "B"

# Mostrar el grupo al que pertenece
if gender == "F":
    gender_complete = "mujer"
else:
    gender_complete = "hombre"
print(f"Usted pertenece al grupo {group} (sexo: {gender_complete}).")