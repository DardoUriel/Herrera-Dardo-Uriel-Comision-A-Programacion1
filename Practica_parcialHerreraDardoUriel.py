# Se plantea la ide de una aplicacion de una linea de credito 
# Movistar donde el usuario pueda registrarse, loguearse, elegir un plan, ver su plan y darse de baja de su plan, tambien eliminar su cuenta.
# Registrarse: debe pedir crear un usuario y una contraseña, pedirlo una sola vez.
# Loguearse: pide usuario y contraseña y valide que coincidan con las de registro (3 intentos), en el caso de que no coincidan 
# las contraseñas pasados los 3 intentos se debe mostrar un mensaje y salir del programa.
# Elegir un plan: el usuario tiene acceso a 3 planes a elegir dependiendo de la cantidad de gigas que se deseen.
# Los gigas tienen un precio determinado que se calculan después de elegir el plan
# La opción ver mi plan, si se tiene un plan, va a mostrar el plan actual y los gigas totales.
# La opcion darse de baja va a dar dos opciónes nuevas, dar de baja el plan y dar de baja la cuenta.
# La ultima opción salir de programa sale del programa (wow!!)
registered_bool = None
gigas = None
global user
global password
opcion_plan = None
def menu(user, password, gigas, opcion_plan):
    print("\nSeleccione una opcion")    
    print("1) Elegir un plan ")    
    print("2) Ver mi plan ")
    print("3) Dar de baja")    
    print("4) Cerrar Sesion")
    opcion = input()
    if opcion == "1" or opcion.upper() == "ELEGIR UN PLAN": #selector de planes
        while True:
            gigas = int(input("Ingresar cantidad de gigas: "))
            if gigas < 1:
                print("Cantidad de Gigas invalida!!")
                continue
            print(f"1) Plan de {gigas}gb por 1 mes + 10Gb DE REGALO !! +  Whatsapp GRATIS!")
            print(f"2) Plan de {gigas}gb por 4 mes + 6Gb DE REGALO !! +  Whatsapp GRATIS!")
            print(f"3) Plan de {gigas}gb por 6 mes + 3Gb DE REGALO !! +  Whatsapp GRATIS!")
            print(f"4) Plan de {gigas}gb por 12 mes + 2Gb DE REGALO !! +  Whatsapp GRATIS!")
            opcion_plan = input()
            if opcion_plan != "1" and opcion_plan != "2" and opcion_plan != "3" and opcion_plan != "4": #corrobora las opciones
                print("Opción invalida!!")
                continue
            print(f"\nOpción elegida: {plan_select(gigas, opcion_plan)}") #se llama a la funcion plan_select para obtener el string del precio final
            menu(user, password, gigas, opcion_plan) #se llama al menú de vuelta
    elif opcion == "2" or opcion.lower() == "ver mi plan":
        if gigas != None:
            print(f"\nSu plan actual es: {plan_select(gigas, opcion_plan)}")
            menu(user, password, gigas, opcion_plan)
        else:
            print("\nNo tiene ningún plan activo")
            menu(user, password, gigas, opcion_plan)#se llama al menú de vuelta
    elif opcion == "3" or opcion.lower() == "dar de baja":
        while True:
            print("\n1) Dar de baja la cuenta")
            print("2) Dar de baja el plan")
            opcion_1 = input()
            if opcion_1 == "1":
                user = None
                password = None
                print("La cuenta fué eliminada exitosamente!!")
                main() #se vuelve a iniciar el codigo principal (inicio limpio)
            elif opcion_1 == "2":
                gigas = 0 #se elimina el plan
                print("El plan fue eliminado exitosamente!!")
                break
    elif opcion == "4" or opcion.lower() == "cerrar sesion":
        exit()

def plan_select(gigas, opcion): #devuelve el string hecho del calculo del precio
    if opcion == "1":
        return f"Plan de {gigas}gb por 1 mes + 10Gb DE REGALO !! +  Whatsapp GRATIS!, total: ${gigas * 15}"
    elif opcion == "2":
        return f"Plan de {gigas}gb por 4 mes + 6Gb DE REGALO !! +  Whatsapp GRATIS!, total: ${gigas * 15}"
    elif opcion == "3":
        return f"Plan de {gigas}gb por 6 mes + 3Gb DE REGALO !! +  Whatsapp GRATIS!, total: ${gigas * 15}"
    elif opcion == "4":
        return f"Plan de {gigas}gb por 12 mes + 2Gb DE REGALO !! +  Whatsapp GRATIS!, total: ${gigas * 15}"

def main():
    registered_bool = False
    while True:
        print("Ya está registrado??")
        print("1) Si")
        print("2) No")
        registered = input()
        if registered == "1" or registered.upper() == "SI":
            registered_bool = True
        elif registered == "2" or registered.upper() == "NO":
            registered_bool == False
        else:
            print("Opción invalida!!")
            continue
        if not registered_bool:
            user = input("\nEscriba su nuevo usuario: ") #registro simple
            password = input("Escriba su nueva contraseña: ")
            print("Ya está registrado!!")
        print("\nAhora debe iniciar sesión")
        for i in range(2, -1, -1): # 3 intentos
            print(f"Tiene {i+1} intentos!")
            user_log = input("Escriba su usuario: ")
            password_log = input("Escriba su contraseña: ")
            if user_log == user and password_log == password: #se compara con el usuario ya creado
                print(f"\nSesión iniciada, bienvenido {user}!!\n")
                break
            print("Usuario o contraseña incorrectas!!!")
        else:
            print("Se quedó sin intentos!!")
            exit() 
        menu(user, password, gigas, opcion_plan)  
print("Bienvenido a movistar planes!!!\n")
main()     
