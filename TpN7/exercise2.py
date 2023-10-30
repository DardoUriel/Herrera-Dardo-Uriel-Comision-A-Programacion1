#2.	Crea un programa que tome una lista de palabras como entrada y 
#las ordene alfabéticamente en orden ascendente 
#utilizando el método de ordenamiento de selección.

def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        arr[i], arr[min_index] = arr[min_index], arr[i]

new_list = ["g", "b" , "d" ,"c" , "f" , "e" , "a" , "h"]
selection_sort(new_list)
print(new_list)