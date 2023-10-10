"""11-	La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.
•	Ingredientes vegetarianos: Pimiento y tofu.
•	Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. 
Solo se puede elegir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. 
Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.
"""
option = input("¿Quiere una pizza vegetariana (V) o no vegetariana (NV)? ").upper()
ingredients = "mozzarella y tomate"


if option == "V":
    print("Ingredientes vegetarianos disponibles: Pimiento y Tofu")#Verificar la elección del usuario y mostrar los ingredientes disponibles
    choice = input("Elija un ingrediente vegetariano: ").capitalize()
    if choice in ["Pimiento", "Tofu"]:
        ingredients += f", {choice}"
        is_vegetarian = True
    else:
        print("Esa opción no es válida.")
        is_vegetarian = False
elif option == "NV":
    print("Ingredientes no vegetarianos disponibles: Peperoni, Jamón y Salmón")
    choice = input("Elija un ingrediente no vegetariano: ").capitalize()
    if choice in ["Peperoni", "Jamón", "Salmón"]:
        ingredients += f", con {choice}"
        is_vegetarian = False
    else:
        print("Esa opción no es válida.")
        is_vegetarian = True
else:
    print("Esa opción no es válida.")
    is_vegetarian = None
if is_vegetarian is not None:
    tipe_pizza = "vegetariana" if is_vegetarian else "no vegetariana"
    print(f"Usted ha elegido una pizza {tipe_pizza} con los siguientes ingredientes: {ingredients}")
