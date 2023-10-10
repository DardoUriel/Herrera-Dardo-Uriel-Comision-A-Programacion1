"""12-	Escriba un programa que pida el año actual y un año cualquiera y que escriba cuántos años han pasado desde ese año o cuántos años faltan para llegar a ese año."""
actual_year = int(input("Ingrese el año actual: "))
any_year = int(input("Ingrese otro año cualquiera: "))
if actual_year == any_year:
    print("Los años ingresados son iguales!!")
elif actual_year > any_year: #desde aqui se comprueba cual es mayor para saber si faltan años o ya han pasado
    print(f"Han pasado {actual_year-any_year} años desde el año {any_year}")
else:
    print(f"Faltan {any_year-actual_year} años para el año {any_year}")