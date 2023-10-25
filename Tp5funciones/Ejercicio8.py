"""8.	Diseñar una función que calcule el área y el perímetro de una circunferencia. 
Utiliza dicha función en un programa principal que lea el radio de una circunferencia y muestre su área y perímetro."""
from functions import area_and_perimeter
while True:
    radio = float(input("Escriba el radio de la circunferencia: "))
    if radio >= 0: #se corrobora que sea un número positivo
        break
    else:
        print("Tiene que ser un número positivo!!")
        continue       
perimeter, area = area_and_perimeter(radio) #se devuelven los valores de área y de perímetro
print(f"El área de la circunferencia es: {round(area,3)} y su perimetro es de: {round(perimeter,3)}")
