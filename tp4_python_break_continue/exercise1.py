#1.	Escriba un programa que acepte una secuencia de líneas e imprima todas las líneas convertidas en mayúsculas. 
#Deje una línea en blanco para indicar que ha finalizado la entrada de líneas.
while True:
    line = input("Ingrese una línea (o deje en blanco para finalizar): ")
    
    if line== "":
        break  #sale si esta en blanco
    else:
        print(line.upper())#ingresar valores