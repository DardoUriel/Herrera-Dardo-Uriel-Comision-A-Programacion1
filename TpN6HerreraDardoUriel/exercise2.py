#2.	A continuación, solicitar al usuario que ingrese un número y, si el número está en la lista, eliminar su primera ocurrencia. 
#Mostrar un mensaje si no es posible eliminar.
numbers  = [1,2,3,4,5,6,7,8,9,1,2,3,4]
number = int(input("Ingrese un numero: "))
if number in numbers:
    numbers.remove(number)
    for i in numbers:
        print (i , end= " ")
else:
    print("no es posible eliminar: ")