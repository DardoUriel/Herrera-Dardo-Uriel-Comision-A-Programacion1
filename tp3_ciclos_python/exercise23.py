#23-	Crear un programa que permita al usuario ingresar 
#los montos de las compras de un cliente 
#(se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), 
#cortando el ingreso de datos cuando el usuario ingrese el monto 0.
customer=1
while True:
    amount = int(input(f"ingrese un monto del cliente {customer}: "))
    customer+=1
    if amount==0:
        break