'''4.	Escribe un programa que tome una lista de cadenas como entrada y 
las ordene en orden ascendente según su longitud.
Puedes utilizar el método de ordenamiento de inserción.'''



def insertion_sort_by_length(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and len(key) < len(arr[j]):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

new_list = ["hola" , "como estas" ,"chau" , "nos vemos" , "bye" , "hello" , "goodbye"]
insertion_sort_by_length(new_list)
print(new_list)