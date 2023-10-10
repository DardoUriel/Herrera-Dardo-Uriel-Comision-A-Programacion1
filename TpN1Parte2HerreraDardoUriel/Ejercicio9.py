"""9.	Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto deberá pagar finalmente por su compra."""
price = float(input("Cuánto es el precio sin el descuento?: "))
discount = price * 0.15 #calculo de descuento
print(f"El precio con descuento es de: {round(price - discount,2)}")