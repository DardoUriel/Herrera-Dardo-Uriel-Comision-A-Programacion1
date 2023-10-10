"""10.	Un alumno desea saber cual será su calificación final en la materia de Algoritmos. Dicha calificación se compone de los siguientes porcentajes:
55% del promedio de sus tres calificaciones parciales.
30% de la calificación del examen final.
15% de la calificación de un trabajo final.
"""
parcial1= float(input("Nota del primer parcial: "))
parcial2= float(input("Nota del segundo parcial: "))
parcial3= float(input("Nota del tercer parcial: "))
average = (parcial1 + parcial2 + parcial3) / 3 #calculo del promedio
final_exam = float(input("Nota del examen final: "))
final_assignment = float(input("Nota del trabajo final: "))
final_grade = round(average * 0.55 + final_exam * 0.30 + final_assignment * 0.15, 2) #calculo de la nota total
print(f"Tu nota final es de: {final_grade}")
