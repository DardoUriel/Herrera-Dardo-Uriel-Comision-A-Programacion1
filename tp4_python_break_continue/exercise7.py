'''7.	Crea un programa que muestre un menú de opciones (por ejemplo, opciones 1, 2, 3). 
Utiliza un bucle while para permitir al usuario seleccionar una opción. Si el usuario ingresa "0", 
utiliza break para salir del bucle 
(Mostrar un mensaje por cada opción elegida).
'''
while True:
    option=int(input("ingrese una opcion: "))#ingresa una opcion
    if option==1:
        print(f"opcion {option}")
    elif option==2:
        print(f"opcion {option}")
    elif option==3:
        print(f"opcion {option}")
    elif option==0:
        print(f"opcion {option}")#sale si se ingresa 0
        break
    else:
        continue
    