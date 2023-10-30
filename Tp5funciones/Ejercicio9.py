"""9.	Crear una subrutina llamada “login”, que recibe un nombre de usuario y una contraseña y te devuelve Verdadero 
si el nombre de usuario es “usuario1” y la contraseña es “asdasd”. Además recibe el número de intentos que se ha intentado hacer login y si
no se ha podido hacer login incremente este valor.
Crear un programa principal donde se pida un nombre de usuario y una contraseña y se intente hacer login, 
solamente tenemos tres oportunidades para intentarlo.
"""
import sys
sys.path.append("C:/Users/FlowUser/Desktop/UTN/ProgrmacionRepositorio/Herrera-Dardo-Uriel-Comision-A-Programacion1/Funciones")
from functions import login
tries = 0
while True:
    print(f"Intento n{tries+1}")
    user = input("Escriba el usuario: ")
    password = input("Escriba la contraseña: ")
    checker, tries = login(user, password, tries) #se llama a la función logi, y trar el verificador si está correcto y los intentos aumentados si hubo algún error
    if tries == 3:
        print("Se quedó sin intentos!!\n") #se queda sin intentos
        break
    elif checker == True:
        print("Accedió como usuario1 exitosamente!!\n") #se sale el programa si se encuentra la cuenta y contraseña
        break
    else:
        print("Cuenta o contraseña incorrecta!!\n") #se sale si se queda sin intentos

