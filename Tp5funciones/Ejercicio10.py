"""10.	Escribir una función que aplique un descuento a un precio. 
Esta función tiene que recibir un diccionario con los precios y porcentajes del carrito de compra, 
aplicar los descuentos a los productos del carrito  y devolver el precio final de la compra."""
from functions import discount_applier
prices_and_discounts = { #los precios y los descuentos respectivamente, menor el precio mayor el descuento
    10000:10,
    5000:50,
    1000:90,
    500:95
}
discount_applier = discount_applier(prices_and_discounts) #se llama a la funcion que devuelve un array con los precios con descuento
total = 0
for i in discount_applier:
    print("Precio con desceunto: ", i)
    total += i #se calcula el precio total
print(f"El precio total es de: {total}")
