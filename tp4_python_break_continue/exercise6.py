
numbers = [1,2,3,4,5,6,7,8,9,10]
#6.	Crea una lista de números y utiliza un bucle for para encontrar un número específico. 
#Cuando encuentres el número, usa break para salir del bucle.
look_for = int(input("ingrese un numero a buscar"))#buscar un numero
for i in range(1,len(numbers)):
    if look_for == i:
        print(f"{look_for} se encontro el numero")#se encuentra el numero
    else:
        continue#sigue el bucle