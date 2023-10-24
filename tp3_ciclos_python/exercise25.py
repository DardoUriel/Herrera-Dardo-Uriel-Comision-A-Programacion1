#25-	Dado un número entero positivo, mostrar su factorial. 
#El factorial de un número se obtiene multiplicando todos los números enteros
#positivos que hay entre el 1 y ese número. 
#El factorial de 0 es 1.
num = int(input("ingrese un numero: "))
aux=1
if num>0:
    for i in range(1,num+1):
        aux*=i
print(f"el factorial es {aux}")