"""15.	Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos.
El tiempo de viaje hasta llegar a otra ciudad B es de T segundos. Escribir un algoritmo que determine la hora de llegada a la ciudad B."""
hours = int(input("Ingrese la hora: "))
minutes = int(input("Ingrese los minutos: "))
seconds = int(input("Ingrese los segundos: "))
distance = int(input("Ingrese los segundos de distancia hasta la otra ciudad: "))
departure_seconds = (hours * 3600) + (minutes * 60) + seconds + distance #la hora de partida en segundos, se suma con los segundos de distancia
end_hour = departure_seconds // 3600
end_minutes = departure_seconds % 3600 // 60
end_seconds = departure_seconds % 3600 % 60 #los segundos totales se formatean a horas
print(f"La hora de llegada a la otra ciudad es: {end_hour:02d}:{end_minutes:02d}:{end_seconds:02d}") #La expresión :02d se utiliza para formatear un número entero (d representa "decimal") de manera que ocupe al menos 2 caracteres, y si el número tiene menos de 2 dígitos, se rellena con ceros a la izquierda para que tenga una longitud de 2 caracteres.