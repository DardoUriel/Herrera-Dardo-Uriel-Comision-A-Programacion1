from functions import*
exit = "" #bucle para el menu de control y llamada a main para comienzo del programa
while True:
    main()                                  
    exit = input("volver al menu? s/n: ")
    if exit.lower() == "n":
        break
        
