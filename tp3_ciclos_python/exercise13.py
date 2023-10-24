#13-	Escribir un programa que muestre el eco de todo
#o que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
while True:
    entrada = input("Introduce algo (o escribe 'salir' para terminar): ")
    if entrada.lower() == "salir":
        break
    else:
        print("Eco:", entrada)