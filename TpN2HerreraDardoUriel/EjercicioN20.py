"""20-	Determinar si un alumno aprueba o reprueba un curso, sabiendo que aprobara si su promedio de cuatro (4) notas, es mayor o igual a 6; 
caso contrario saldrá desaprobado."""
grade1 = float(input("Escriba la primer nota a promediar: "))
grade2 = float(input("Escriba la segunda nota a promediar: "))
grade3 = float(input("Escriba la tercer nota a promediar: "))
grade4 = float(input("Escriba la cuarta nota a promediar: "))
final_grade = (grade1 + grade2 + grade3 + grade4) / 4
if final_grade >= 6:
    print(f"Aprobado con {round(final_grade,2)}")
else:
    print(f"Desaprobado con {round(final_grade,2)}")