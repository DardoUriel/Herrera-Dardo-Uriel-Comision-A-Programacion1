"""8.	Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, el vendedor desea saber cuanto dinero obtendrá por concepto de
comisiones por las tres ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones."""
wage = float(input("Cuánto es su sueldo base?: "))
sell_1= float(input("De cuánto es el valor de la primer venta?: "))
sell_2= float(input("De cuánto es el valor de la segunda venta?: "))
sell_3= float(input("De cuánto es el valor de la tercer venta?: "))
total_extra = (sell_1 + sell_2 + sell_3) * 0.1 #calculo del extra
print(f"El total de sueldo que tendrá este mes es de: {round(wage + total_extra , 2)}")