"""4-	Crear un programa que permita al usuario elegir un candidato por el cual votar. 
Las posibilidades son: candidato A por el partido rojo, candidato B por el partido verdad, candidato C por el partido azul.
Según el candidato elegido (A, B o C) se debe imprimir el mensaje: ‘Usted ha votado por el partido [color del candidato elegido]."""
print("Ingrese 'A' para votar al partido rojo, 'B' para votar al partido verde o 'C' para votar al partido azul")
vote = input()
if vote.upper() == "A":
    print("Usted ha votado al partido rojo!!")
elif vote.upper() == "B":
    print("Usted ha votado al partido verde!!")
elif vote.upper() == "C":
    print("Usted ha votado al partido azul!!")
else:
    print("Voto invalido, vuelva a intentarlo!")
