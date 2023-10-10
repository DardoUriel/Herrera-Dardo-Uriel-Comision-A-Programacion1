"""18-	Preguntar al usuario el total de horas trabajadas en el mes y el salario por hora.
La jornada de trabajo mínima es de 48 horas. Calcular, dadas las horas trabajadas, si trabajó horas extras y mostrar esta cantidad.
Mostrar su salario total, tomando en cuenta que las horas extras serán pagadas un 10% más que las horas laborales comunes."""
hours_worked = int(input("Ingrese el total de horas trabajadas en el mes: "))
hourly_rate = float(input("Ingrese el salario por hora: "))
if hours_worked > 48: #Calcular las horas extras
    overtime_hours = hours_worked - 48
else:
    overtime_hours = 0
if overtime_hours > 0: #Se calcula el salario total
    regular_pay = 48 * hourly_rate
    overtime_pay = overtime_hours * hourly_rate * 1.10  # Se paga un 10% adicional por horas extras
    total_pay = regular_pay + overtime_pay
else:
    total_pay = hours_worked * hourly_rate
print(f"Horas extras trabajadas: {overtime_hours} horas")
print(f"Salario total: ${round(total_pay,2)}")