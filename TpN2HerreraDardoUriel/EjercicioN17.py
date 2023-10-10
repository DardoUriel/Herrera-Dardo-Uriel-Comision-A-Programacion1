"""17-	Requerir al usuario que ingrese un día de la semana e imprimir un mensaje si es lunes, otro mensaje diferente si es viernes, otro mensaje diferente si es sábado o domingo. 
Si el día ingresado no es ninguno de esos, imprimir otro mensaje."""
week_day = input("Escriba un día de la semana: ").upper()
if week_day == "LUNES":
    print("El lunes es feo")
elif week_day == "VIERNES":
    print("El viernes es epico!")
elif week_day == "SABADO" or week_day == "DOMINGO":
    print(f"El {week_day.capitalize()} está dentro del fin de semana, muy epico!!")
else:
    print(f"El día {week_day.capitalize()} o no existe o no me importa")