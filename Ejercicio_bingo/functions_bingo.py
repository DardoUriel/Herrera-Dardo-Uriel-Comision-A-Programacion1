def validate_num(n, card, row):
    if n in row:
        print("Valor repetido en fila!")
        return False
    for x in card:
        for c in x:
            if n == c:
                print("Valor repetido en otra fila!")
                return False
    return True


def random_validator(num, matrix):
    for i in range(0,5):
        row = matrix[i]
        
        for j in range(0,5):
            if row[j] == num:
                row[j] = "x"

        matrix[i] = row

    return matrix

def row_validator(matrix):
    for row in matrix:
        count = 0
        print(row)
        for i in range(0,5):
            if row[i] == "x":
                count+=1
        if count == 5:
            return True
    return False


def column_validator(matrix):
    count = 0
    index = 0
    for row in matrix:
        if row[index] == "x": 
            count+=1
        else: 
            return False
    if count == 5: 
        return True
    else: return False


def diagonal_validator(matrix):
    count = 0
    index=0
    for row in matrix:
        if row[index] == "x":
            count+=1
        else: 
            index+=1
    if count == 5:
        return True

