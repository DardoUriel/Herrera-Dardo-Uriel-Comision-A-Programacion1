"""21.	Una pareja de motociclistas necesita hacer ciertos cálculos antes de emprender un viaje en moto, para saber cuántos tanques de combustible consumirá el viaje entero.
Para eso deben ingresar: cuántos kilómetros puede recorrer su moto con 1 litro de combustible, qué capacidad (en litros) tiene el tanque y cuántos kilómetros en total recorrerán.
Hacer un programa que solicite los datos necesarios y luego informe la cantidad de tanques de combustible necesarios.
"""
gas_for_kilometer = float(input("Cuántos kilometros puede recorrer su moto con 1 litro de combustible?: "))
tank_capacity = float(input("Ingrese la capacidad del tanque en litros: "))
kilometers_traveled = float(input("Ingrese cuántos kilómetros en total recorrerán: "))
nesesary_tanks = kilometers_traveled / (gas_for_kilometer * tank_capacity)# se calcula la cantidad de tanques de combustible necesarios
print(f"Para el viaje de {kilometers_traveled} kilómetros, necesitarán {round(nesesary_tanks, 2)} tanques de combustible.")