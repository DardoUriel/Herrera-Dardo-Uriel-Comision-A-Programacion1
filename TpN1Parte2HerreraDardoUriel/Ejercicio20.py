"""20.	Hacer otra versión del programa, pero esta vez almacenado todo en una única variable con formato DDMMAAA."""
birthday = input("Ingrese su fecha de nacimiento en formato DDMMAAAA (ejemplo: 01012000): ") #se pide la fecha en formato
day = int(birthday[:2])
month = int(birthday[2:4])#se extraen las partes del cumpleaños
year = int(birthday[4:])
print(f"Fecha de nacimiento: {day:02d}/{month:02d}/{year}")#se muestra la fecha en formato
