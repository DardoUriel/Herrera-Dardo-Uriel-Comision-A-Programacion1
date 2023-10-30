#4.	Solicitar al usuario otro número y crear una lista con los elementos de la lista original, que sean menores que el número dado. 
#Imprimir esta nueva lista, iterando por ella.
import random
original = [50,60,20,10,30,75,20,44,10]
new_list = []
number = int(input("Ingrese un numero: "))
for i in original:
    if number>i:
        new_list.append(i)
new_list.sort()
print(f"nueva lista: {new_list}")