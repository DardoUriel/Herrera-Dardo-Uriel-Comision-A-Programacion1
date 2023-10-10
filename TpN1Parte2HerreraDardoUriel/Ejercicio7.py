"""7.	Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde. Por ejemplo: 1000 minutos son 16 horas y 40 minutos."""
minutes = int(input("Escriba la cantidad de minutos para dividirlo en horas y minutos: "))
hours = minutes // 60 #calculo de horas enteras
rest = minutes % 60 #resto es minutos que sobran
print(f"En {minutes} minutos hay {hours} horas y {rest} minutos!!!")