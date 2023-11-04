def menu():
    # Solicitar al usuario una opción
    option = int(input("1) Demo Mutante\n2) Demo No Mutante\n3)Demo Diagonales comunes\n4)Demo Diagonales invertidas\n5)Ingresar matriz propia\nIngresar una opcion: "))
    matrix = []

    if option == 1:
        # Matriz de demostración de mutante
        mutant =  ['ATGCGA','CAGTGC','TTATGT','AGAAGG','CCCCTA','TCACTG']
        return mutant

    elif option == 2:
        # Matriz de demostración de no mutante
        not_mutant = ['ATGCGA','CAGTGC','TTATGT','ATACGT','CGCCTA','TCACTG']
        return not_mutant
    elif option == 3:
        # Matriz de demostración de todas las diagonales comunes
        diagonals1=['ATGCGA','CACGAC','TCGACT','CGACTG','GACTTA','ACTCTG']
        return diagonals1
    elif option == 4:
        # Matriz de demostración de todas las diagonales invertidas
        diagonals2= ['ACGCGA','TACGAC','CTACGT','CCTACG','GACTAC','ACTCTA']
        return diagonals2
    elif option == 5:
        # Permitir al usuario ingresar su propia matriz
        print("Ingresa tu arreglo de 6 cadenas:")
        for i in range(6):
            sub_matrix = []
            j=0
            while j<=4:
                
                print(f"ingresar cadena:")
                letter  = input()
                if len(letter) == 6:
                    for k in range(6):
                        if letter[k].upper()  != 'A' and letter[k].upper() != 'C' and letter[k].upper()  != 'T' and letter[k].upper()  != 'G':
                            print("las unicas letras valida son A T C G")
                            j = j-1
                            continue
                        j=j+1
                else:
                    print("el tamño de la cadena ingresada debe ser de 6 caracteres")
                    j = j-1
                    continue
                        
            matrix.append(letter)
        return matrix

    else:
        # Opción incorrecta
        print("opcion incorrecta.")
        return matrix
def count_diags(compare_dna):
    count_times = 0
    diagonals = []
    
    # Diagonales de izquierda a derecha (superiores)
    for i in range(1, 6):
        diagonal = [compare_dna[j][j - i] for j in range(i, 6)]
        diagonals.append(diagonal)

    # Diagonales de izquierda a derecha (inferiores)
    for i in range(5):
        diagonal = [compare_dna[j][j + i] for j in range(5 - i)]
        diagonals.append(diagonal)

    # Diagonales invertidas (superiores)
    for i in range(1, 6):
        diagonal = [compare_dna[j][5 - j + i] for j in range(i, 6)]
        diagonals.append(diagonal)

    # Diagonales invertidas (inferiores)
    for i in range(5):
        diagonal = [compare_dna[j][5 - j - i] for j in range(5 - i)]
        diagonals.append(diagonal)

    detected_diagonals = set()  # Para evitar duplicados
    for diagonal in diagonals:
        for i in range(len(diagonal) - 3):
            if diagonal[i] == diagonal[i + 1] == diagonal[i + 2] == diagonal[i + 3]:
                sequence = ''.join(diagonal[i:i + 4])
                if sequence not in detected_diagonals:
                    print(f"Coincidencia en diagonal detectada: {sequence}", end=" ")
                    print("")
                    detected_diagonals.add(sequence)
                    count_times += 1

    return count_times




def mutant_in_row(matrix):
    # valida si hay  mutantes en cada fila
    count = 0
    for i in range(6):
        dna = matrix[i]
        if is_mutant(dna):
            print(f"coincidencia en fila {i} detectada")
            count += 1
    return count

def mutant_in_column(matrix):
    # valida si hay mutantes en cada columna
    count = 0
    for i in range(6):
        dna = [matrix[j][i] for j in range(6)]
        if is_mutant(dna):
            print(f"coincidencia en columna {i} detectada")
            count += 1
    return count

def is_mutant(dna):
    # Valida si una secuencia de ADN es mutante
    line = ''.join(dna)
    if "AAAA" in line.upper() or "TTTT" in line.upper() or "CCCC" in line.upper() or "GGGG" in line.upper():
        return True
    else:
        return False

def print_matrix(matrix):
    # Imprime una matriz
    for row in matrix:
        print(' '.join(row))
def main():
    matrix = menu()
    print_matrix(matrix)
    count = mutant_in_row(matrix) + mutant_in_column(matrix) + count_diags(matrix)
    
    # Contar mutantes en diagonales
    if count >= 2:
        print("Es Mutante")
    else:
        print("No es mutante (debe contener más de una coincidencia para ser mutante)")

