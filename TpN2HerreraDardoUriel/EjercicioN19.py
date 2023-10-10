"""19-	Determinar cuánto se debe pagar por una cantidad de lápices considerando que si son 1000 o más, existe un descuento de 7% y teniendo en cuenta que el costo por lápiz es de $60;
de lo contrario no hay descuento."""
quantity_pencils = int(input("Ingrese la cantidad de lápices que desea comprar: "))
cost_without_discount = quantity_pencils * 60 #Se calcula el costo total sin descuento
if quantity_pencils >= 1000: #se ve si hay 1000 o más para el descuento
    discount = cost_without_discount * 0.07 
    total_cost = cost_without_discount - discount
    print(f"El costo total con un descuento del 7% es: ${round(total_cost,2)}")
else:
    print(f"El costo total sin descuento es: ${round(cost_without_discount,2)}")