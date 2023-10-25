def sumar_digitos(num):
    if num%10==num:
        return num
    else:
        return num%10 + sumar_digitos(num//10)
def show_hidden_word(word, empty_word, attempts):
    """_summary_

    Args:
        word (str): palabra completa
        empty_word (list): lista de "_" a completar
        attempts (list): lista de intentos

    Returns:
        list: empty_word actualizado, si se actualizó 
    """
    for i in attempts: 
        if i in word.lower():
            for j in range(len(word)):
                if i == word[j].lower():
                    empty_word[j] = i
    return empty_word
            
#--------FUNCIONES TP 5 DEL EJ 1 AL 7------------------------------------------------------
def number_dni_validate(dni_user):
    """
        validar dni
    Args:
        dni_user (str): dni ingresado por el usuario

    Returns:
        bool : True si el numero esta entre 7 y 8 digitos,False sino lo esta 
    """
    if len(dni_user)>8 or len(dni_user)< 7:
        return False
    else:
        return True
def access_last_word(sentence):
    """obtener ultima palabra de un str

    Args:
        sentence (str): cadena de texto ingresada por el usuario

    Returns:
        str : ultima palabra de la cadena ingresada
    """
    array = sentence.split()
    return array[len(array)-1]
    
def validate_format_full_name(full_name):
    """da un foramato especifico a una cadena de texto

    Args:
        full_name (str): nombre completo

    Returns:
        bool :devuelve False solamente si la cantidad de palabras ingresadas es mayor a 3 o menor o igual a 1
    """
    array = full_name.split()
    if len(array) > 3 or len(array) <= 1  :
        return False
    else:
        return True 
def create_identifier(full_name,dni):
    """crea un identificador con el primer nombre, segido de el numero de letras del apellido y los primeros 3 digitods del dni

    Args:
        full_name (str):cadena de texto con nombre completo 
        dni (_type_): dni del usuario 

    Returns:
        str: un identificador con el primer nombre, segido de el numero de letras del apellido y los primeros 3 digitods del dni
    """
    last_name  = access_last_word(full_name)
    first_name = full_name.split()
    first_name = first_name[0]
    return f"{first_name}{len(last_name)}{dni[0]}{dni[1]}{dni[2]}" 
def multiple(num,num2):
    """devuelve si un numero es multiplo de otro pasados por parametro

    Args:
        num (int): numero
        num2 (int): numero

    Returns:
        str: num es multiplo de num2
        str: num no es multiplo de num2
    """
    if num%num2==0:
        return f"{num} es multiplo de {num2}"
    else:
        return f"{num} no es multiplo de {num2}"
    
def half(max,min):
        return (max+min)/2
def letter_spacing(senten):
    new_sentence = ""
    new_sentence2 = ""
    arreglo = senten.split()
    for i in range(len(arreglo)):
        new_sentence += arreglo[i] 


    for i in range(len(new_sentence)):
        x =  new_sentence[i]
        new_sentence2 += (x + " ")
    print(len(new_sentence2))
    return new_sentence2
def max_and_min_value(numbers):
    max = 0
    for i in range(len(numbers)):
        if numbers[i] > max:
            max = numbers[i]
    min = max
    for i in range(len(numbers)):
        if numbers[i]< min:
            min = numbers[i]
    return f"el valor maximo es: {max} y el valor minimo es: {min}"                
#--------FUNCIONES TP 5 DEL EJ 1 AL 7------------------------------------------------------
"""ejercicios del tp5 a partir del 8"""
from math import pi as pi
def area_and_perimeter(radio):
    """usa las formulas de área y perímetro de un círculo y las devuelve a partír del radio

    Args:
        radio (float): radio del círculo

    Returns:
        float, float: perímetro y área respectivamente
    """
    perimeter = 2 * pi * radio
    area = pi * (radio ** 2)
    return perimeter, area

def login(user, password, tries):
    """a partir de un usuario y contraseña, devuelve si son correctas y aumenta la variable tries, aumentandola en 1

    Args:
        user (str): usuario
        password (str): contraseña
        tries (int): intentos ocupados

    Returns:
        bool, int: verificador de igualdad, aparte de los intentos ocupados
    """
    if user == "usuario1" and password == "asdasd":
        return True, tries
    else:
        tries += 1
        return False, tries

def discount_applier(prices_and_discounts):
    """recibe una lista y a la primer llave se le resta el porcentaje el cual es su respectivo valor.

    Args:
        prices_and_discounts (dict): diccionario con sus precios y descuentos

    Returns:
        list: todos los precios actualizados
    """
    discounts = []
    counter = 0
    for i in prices_and_discounts.keys():
        discounts.append(i)
    for i in prices_and_discounts.values():
        discounts[counter] = discounts[counter] - (discounts[counter] * (i / 100)) #formula para calcular el precio menos su debido descuento
        counter +=1
    return discounts

def next_number(num):
    return num+1
def func_applier(num_list):
    """recibe una lista y devuelve el número siguiente de cada elemento en la misma lista, usando la funciión next_number

    Args:
        num_list (list): lista con números

    Returns:
        list: lista con los siguientes de cada número
    """
    for i in range(len(num_list)):
        num_list[i] = next_number(num_list[i])
    return num_list

def phrase_to_dict(phrase):
    """recibe una frase y devuelve un diccionario con las palabras que contiene y su longitud

    Args:
        phrase (str): frase

    Returns:
        dict: diccionario con las palabras y su longitud
    """
    dict = {}
    words = phrase.split()
    for word in words:
        dict[word] = len(word)
    return dict
import math

def modulus_of_a_vector(vector):
    """
    Calcula el módulo de un vector tridimensional.
    
    Args:
        vector (list): Una lista con las componentes del vector en el orden (x, y, z).
    
    Returns:
        float: El módulo del vector.
    """
    if len(vector) != 3:
        raise ValueError("El vector debe tener exactamente 3 componentes.")
    
    x, y, z = vector
    modulus = math.sqrt(x**2 + y**2 + z**2)
    return modulus

def prime_detecter(num):
    """
    Recibe un número entero y devuelve si es primo o no.
    
    Args:
        num (int): Número entero a evaluar.
    
    Returns:
        bool: True si el número es primo, False en caso contrario.
    """
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True

def factorials(nums):
    """
    Recibe una lista de números enteros y devuelve una lista con el factorial de cada uno.
    
    Args:
        nums (list): Lista de números enteros.
    
    Returns:
        list: Lista con el factorial de cada número.
    """
    factorials = []
    for i in range(len(nums)):
        factorials.append(math.factorial(nums[i]))
    return factorials

def count_digit_occurrences(number, digit):
    """
    Recibe un número entero y devuelve la cantidad de veces que aparece un dígito.
    
    Args:
        number (str): Número entero a evaluar.
        digit (str): Dígito a evaluar.
    
    Returns:
        int: Cantidad de veces que aparece el dígito.
    """
    count = 0
    for character in number:
        if character == digit:
            count += 1
    return count