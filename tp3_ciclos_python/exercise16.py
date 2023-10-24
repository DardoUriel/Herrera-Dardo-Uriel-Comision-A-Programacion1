#16-	Escriba un programa que pregunte cuántos números se van a introducir, 
#pida esos números y escriba cuántos negativos ha introducido.

amount = int(input("ingrese la cantidad de numeros que quiere: "))
cont=0
for i in range(amount):
    number= int(input("ingrese un numero: "))
    if number<0:
        cont+=1
print(f"se ingreso {cont} numeros negativos")