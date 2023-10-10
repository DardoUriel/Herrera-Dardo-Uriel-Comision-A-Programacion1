"""19.	Solicitar al usuario que ingrese el día, mes y año de su nacimiento y almacenar cada uno de ellos en una variable numérica (en total, tres variables diferentes). 
Finalmente, mostrar la fecha en formato dd/mm/aaaa."""
day = int(input("Ingrese el día de su nacimiento: "))
month = int(input("Ingrese el mes de su nacimiento: "))
year = int(input("Ingrese el año de su nacimiento: "))
print(f"Su fecha de nacimiento con formato: {day:02d}/{month:02d}/{year}")#La expresión :02d se utiliza para formatear un número entero (d representa "decimal") de manera que ocupe al menos 2 caracteres, y si el número tiene menos de 2 dígitos, se rellena con ceros a la izquierda para que tenga una longitud de 2 caracteres.