##1.	Solicitar al usuario que ingrese números, estos deben guardarse en una lista. 
#Para finalizar el usuario debe ingresar 0, el cual no debe guardarse.
numbers = []
while True:
    number = int(input("Ingrese un numero: "))
    if number==0:
        print("Saliendo..")
        break
    else:
        numbers.append(number)
for i in numbers:
    print(i , end = " ")