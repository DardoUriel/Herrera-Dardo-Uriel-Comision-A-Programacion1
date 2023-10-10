"""1.	Calcular el perímetro y área de un rectángulo dada su base y su altura."""
base = float(input("Escriba la base del rectángulo en metros: "))
height = float(input("Escriba la altura del rectángulo en metros: "))
print(f"El perimetro del rectángulo es: {base*2 + height*2} metros")
print(f"El área del rectángulo es: {base*height} metros cuadrados")