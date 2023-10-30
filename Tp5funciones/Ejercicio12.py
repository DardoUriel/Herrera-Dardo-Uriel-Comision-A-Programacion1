"""12.	Escribir una función que reciba una frase y devuelva un diccionario con las palabras que contiene y su longitud."""
import sys
sys.path.append("C:/Users/FlowUser/Desktop/UTN/ProgrmacionRepositorio/Herrera-Dardo-Uriel-Comision-A-Programacion1/Funciones")
from functions import phrase_to_dict
phrase = input("Escriba una frase: \n")
print("Frase a diccionario: \n" , phrase_to_dict(phrase))
