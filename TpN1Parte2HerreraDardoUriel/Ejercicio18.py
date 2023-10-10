"""18.	Hacer un programa que solicite al usuario cuánto costó una cena en un restaurante.
A ese valor, sumarle un 6.2% en concepto de servicio y un 10% de propina. Imprimir en pantalla el monto final a pagar."""
base_value = float(input("Cuánto costó la cena en el restaurante?: "))
total_value = base_value + (base_value * 0.062) + (base_value * 0.10)#se calcula el total
print(f"El valor total, sumados el servicio u el 10% de propina es de: ${round(total_value, 2)}")
