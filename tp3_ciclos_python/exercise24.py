#24-	Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto.
#Al finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el total de $1000,
#se le debe aplicar un 10% de descuento.
while True:
    mount=int(input("ingrese un monto: "))
    if mount >0:
        if mount>10000:
            aux=mount*0.10
            mount+=aux
        print(f"el monto a pagar es {mount}")
        break