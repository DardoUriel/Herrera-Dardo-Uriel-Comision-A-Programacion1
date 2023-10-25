"""12.	Escribir una función que reciba una frase y devuelva un diccionario con las palabras que contiene y su longitud."""
from functions import phrase_to_dict
phrase = input("Escriba una frase: \n")
print("Frase a diccionario: \n" , phrase_to_dict(phrase))
