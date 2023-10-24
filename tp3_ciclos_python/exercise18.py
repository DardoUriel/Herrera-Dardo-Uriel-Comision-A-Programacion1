#18-	Crear un algoritmo que muestre los primeros 10 números de la sucesión de Fibonacci. 
#La sucesión comienza con los números 0 y 1 y, a partir de éstos, 
#cada elemento es la suma de los dos números anteriores en la secuencia: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…
lista =[]
for i in range(10):
    if i == 0 or i==1:
        lista.append(i)
        print(lista[i])
    else:
        aggregate = (lista[i-2])+(lista[i-1])
        lista.append(aggregate)
        print(lista[i])