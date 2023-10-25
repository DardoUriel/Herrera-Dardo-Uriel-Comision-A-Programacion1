'''
2.Escribir una función que, dado un string, retorne la longitud de la última palabra.
Se considera que las palabras están separadas por uno o más espacios.
También podría haber espacios al principio o al final del string pasado por parámetro
'''
from ..functions import access_last_word
words = input("oracion: ")
print(access_last_word(words))#retorna la ultima palabara de una cadena ingresada y se muestra

