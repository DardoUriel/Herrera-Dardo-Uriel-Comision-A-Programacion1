import random, time
from functions_bingo import *

while True:
    card = []

    for i in range(0, 5):
        row = []
        for j in range(0, 5):
            while True:
                n = int(input(f"Ingrese n entre (0 y 75) para posicion [{i}] [{j}]: "))
                if n < 1 or n > 75:
                    print("Valor inválido (entre 0 y 75) !")
                    continue

                if validate_num(n, card, row) == False:
                    continue

                row.append(n)
                print(row)
                break
        card.append(row)
    random_numbers = []
    while True:
        #Mostrar bingo
        print(f"BINGO: ") 
        for e in card:
            print(e)
        time.sleep(0)
        #Numero random que no se repita
        random_num = random.randint(1, 75)
        while random_num in random_numbers:
            random_num = random.randint(1, 75)

        #llevarlo al array y mostrarlo
        random_numbers.append(random_num)
        print(f"Número random: {random_num}")
        
        #Nuevo card con valores modificados
        card = random_validator(random_num,card)
        
        #chekear fila completa
        if row_validator(card):
            print("GANASTE CON FILA")
            break
        
        #chekear columna completa
        if column_validator(card):
            print("GANASTE CON COLUMNA")
            break
        
        #chekear diagonal completa
        if diagonal_validator(card):
            print("GANASTE CON DIAGONAL")
            break

    repeat_game = input("Jugar de nuevo? (s/n): ")
    if repeat_game == "s":
        continue
    else:
        break
